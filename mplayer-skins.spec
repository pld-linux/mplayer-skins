Summary:	MPlayer - skins
Summary(pl):	MPlayer - skóry
Name:		mplayer-skins
Version:	0.50
Release:	0
License:	distributable
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	ftp://mplayerhq.hu/MPlayer/Skin/default.tar.bz2
URL:		http://www.mplayerhq.hu/
Requires:	mplayer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/default-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_skindir	%{_prefix}/share/mplayer/Skin

%description
MPlayer skin.

%description -l pl
Skórka dla MPlayer'a.

%prep
%setup -q -n default

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_skindir}/default

cp -fr {*.fnt,*.png,skin} $RPM_BUILD_ROOT%{_skindir}/default

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_skindir}
