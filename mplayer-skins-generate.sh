#!/bin/sh
# location for mplayer skins
url='ftp://ftp1.mplayerhq.hu/MPlayer/skins/'

# this script must reside inSOURCES dir
set -e
dir=$(dirname "$0")
cd "$dir"
cd ../SOURCES # this makes sure we're in right place

spec='../SPECS/mplayer-skins.spec'
rm -f .listing
wget -r -np -nd -c "$url" --no-remove-listing

add_spec_block() {
	local block="$1"
	sed -i -e "/NEW SKIN MARKER: $block/{
		r $tmpf
		a# NEW SKIN MARKER: $block
		d
	}
	" $spec
}

add_skin() {
	local file="$1"; shift
	local skin="$1"; shift
	local version="$1"; shift
	local tmpf=$(mktemp "${TMPDIR:-/tmp}/fragXXXXXX")

	# add preamble
	sed > $tmpf -e "
	s,@file@,$file,g
	s,@skin@,$skin,g
	s,@version@,$version,g
	" <<'EOF'
%package -n mplayer-skin-@skin@
Summary:	@skin@ skin
Summary(pl.UTF-8):	Skórka @skin@
Version:	@version@
Group:		X11/Applications/Multimedia
Requires:	mplayer-common
Provides:	mplayer-skin

%description -n mplayer-skin-@skin@
@skin@ skin.

%description -n mplayer-skin-@skin@ -l pl.UTF-8
Skórka @skin@.

EOF
	add_spec_block PREAMBLE

	# add %post
	sed > $tmpf -e "
	s,@file@,$file,g
	s,@skin@,$skin,g
	s,@version@,$version,g
	" <<'EOF'
%post -n mplayer-skin-@skin@
if [ "$1" = 1 ]; then
	ln -snf @skin@ %{_skindir}/default
fi

EOF
	add_spec_block POST

	# add %files
	sed > $tmpf -e "
	s,@file@,$file,g
	s,@skin@,$skin,g
	s,@version@,$version,g
	" <<'EOF'
%files -n mplayer-skin-@skin@
%defattr(644,root,root,755)
%{_skindir}/@skin@

EOF
	add_spec_block FILES

	# find free source nr
	last=$(grep -o '^Source[0-9]\+' $spec | sed -s 's,^Source,,' | sort -n | tail -n 1)
	nr=$((last + 1))
	md5=$(awk '{print $1}' $file.md5)
	sed -i -e "/^Source$last:/{n;a\
Source$nr:	$url$file\\
# Source$nr-md5:	$md5
}" $spec

	unpack="bzip2 -dc %{SOURCE$nr}"
	# add unpack
	sed > $tmpf -e "
	s,@file@,$file,g
	s,@skin@,$skin,g
	s,@version@,$version,g
	s,@unpack@,$unpack,g
	" <<'EOF'
@unpack@ | tar -x -C $RPM_BUILD_ROOT%{_skindir}
EOF
	add_spec_block UNPACK

	# add R to base package
	sed > $tmpf -e "
	s,@skin@,$skin,g
	" <<'EOF'
Requires:	mplayer-skin-@skin@
EOF
	add_spec_block REQUIRES

	rm -f $tmpf

	 # delete all leading blank lines at top of file
	sed -i -e '/./,$!d' $spec
}

update_skin() {
	local file="$1"; shift
	local skin="$1"; shift
	local version="$1"; shift

	md5=$(awk '{print $1}' $file.md5)
	sed -i -e "
	/^Source[0-9]\+:.*\/$skin-[0-9]/{
		s/$skin-.*/$file/
		n
		s/\(# Source[0-9]\+-md5:\t\).*/\1$md5/
	}
	" $spec

	sed -i -e "/./{H;\$!d;};x;/%package -n mplayer-skin-$skin/{
		/Version:/s/Version:\t[\.0-9]*/Version:\t$version/
	}" $spec
}

files=$(grep -o '[^ ]*\.tar\.bz2' .listing | sort -u)
for file in $files; do
	skin=$(basename $file .tar.bz2)
	name=$(echo "$skin" | sed -e 's,-[.0-9]\+,,')
	version=$(echo "$skin" | sed -e 's,^.*-\([.0-9]\+\),\1,')
	echo -n "$skin: $name $version "
	if grep -q "^Source[0-9]\+:.*$name-" $spec; then
		echo "HAVE"
		update_skin $file $name $version
	else
		echo "DON'T HAVE"
		add_skin $file $name $version
	fi
done
