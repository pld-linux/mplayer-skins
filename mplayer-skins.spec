Summary:	MPlayer - skins
Summary(pl):	MPlayer - sk�ry
Name:		mplayer-skins
Version:	0.61
Release:	1
License:	distributable
Group:		X11/Applications/Multimedia
Source0:	%{name}-generate.sh
Source1:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/Cyrus-1.2.tar.bz2
# Source1-md5:	4115815cdf2d89552689a4c05fbfe4ee
Source2:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/MidnightLove-1.6.tar.bz2
# Source2-md5:	625e2413dfc9fc9349f51f0d8cc40d2e
Source3:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/WMP6-2.2.tar.bz2
# Source3-md5:	6b8190096abc2ccf432d0300995719c5
Source4:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/avifile-1.6.tar.bz2
# Source4-md5:	680ca462ef537d9df027b70655ca56d5
Source5:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/neutron-1.5.tar.bz2
# Source5-md5:	c1b100fd07cc915562a6a25e1ea92e1b
Source6:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/phony-1.1.tar.bz2
# Source6-md5:	c6023eaf015814a472427d95358802bc
Source7:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/plastic-1.2.tar.bz2
# Source7-md5:	cd9acb1b7f52c4c18bac84e895b8a1b9
Source8:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/proton-1.2.tar.bz2
# Source8-md5:	78ccb5eeafa97b8cace6b4f0e2e22cb9
Source9:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/xanim-1.6.tar.bz2
# Source9-md5:	a9cf60ddbc48dddc005b02491697e4c8
Source10:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/xine-lcd-1.2.tar.bz2
# Source10-md5:	591c10bacaf2766a11d2203d0838f6c7
Source11:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/mentalic-1.2.tar.bz2
# Source11-md5:	c29c760f8a17d0132fc5f5aa9e1a027f
Source12:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/AlienMind-1.2.tar.bz2
# Source12-md5:	1b01ad7ee9c315be202e909ab58b25d2
Source13:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/hwswskin-1.1.tar.bz2
# Source13-md5:	b45ea121d1f31ff5ba8d9d860bafdfa1
Source14:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/XFce4-1.0.tar.bz2
# Source14-md5:	77c05b57d10b91d4f9490801143a0202
Source15:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/OSX-Brushed-2.3.tar.bz2
# Source15-md5:	5e69997c18a265d04bafe1d2b048bf6c
Source16:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/CornerMP-1.2.tar.bz2
# Source16-md5:	66aac74143f424c64b1af41e0c4a0821
Source17:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/CornerMP-aqua-1.4.tar.bz2
# Source17-md5:	09555b7444d89157bbafd79d93151a88
Source18:	http://download.freshmeat.net/themes/plastikmplayer/plastikmplayer-default.tar.gz
# Source18-md5:	2a168d8663ad6f017647ea88258fc978
Source19:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/new-age-1.0.tar.bz2
# Source19-md5:	0b875100252e5846a937fa367b1abd20
Source20:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/Terminator3-1.1.tar.bz2
# Source20-md5:	b6306c4f34ef865fb78407e3ae106224
Source21:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/OSX-Mod-1.1.tar.bz2
# Source21-md5:	8c5e29e14f723b0e7bf5e97a2fe3ecca
Source22:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/Industrial-1.0.tar.bz2
# Source22-md5:	25bf060a79236965a570f009fec4e3ca
Source23:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/DVDPlayer-1.1.tar.bz2
# Source23-md5:	e8c5fcfd35018593eba02057e1d11568
Source24:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/Blue-1.4.tar.bz2
# Source24-md5:	05dd8e4f11a715c9e5d2abf1cdeb907c
Source25:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/ultrafina-1.1.tar.bz2
# Source25-md5:	e7ce4d77e5b40f072302ac397fef7d06
Source26:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/BlueHeart-1.5.tar.bz2
# Source26-md5:	cdb98e53139d6f0b41d48daf4399cec3
URL:		http://www.mplayerhq.hu/
Requires:	gmplayer
Obsoletes:	mplayer-skin-WindowsMediaPlayer6
Obsoletes:	mplayer-skin
Provides:	mplayer-skin
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_skindir	%{_datadir}/mplayer/Skin

%description
Additional skins for MPlayer. Included are skins emulating look of
Windows Media Player, Avfile, Xine and many others.

%description -l pl
Dodatkowe sk�rki dla MPlayera. W pakiecie znajduj� si� sk�rki udaj�ce
wygl�d Widows Media Player, Avifile, Xine i wiele innych.

%package -n mplayer-skin-BlueHeart
Summary:	BlueHeart skin
Summary(pl):	Sk�rka BlueHeart
Version:	1.5
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-BlueHeart
BlueHeart skin.

%description -n mplayer-skin-BlueHeart -l pl
Sk�rka BlueHeart.

%package -n mplayer-skin-Cyrus
Summary:	Cyrus skin
Summary(pl):	Sk�rka Cyrus
Version:	1.2
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-Cyrus
Cyrus skin.

%description -n mplayer-skin-Cyrus -l pl
Sk�rka Cyrus.

%package -n mplayer-skin-MidnightLove
Summary:	MidnightLove skin
Summary(pl):	Sk�rka MidnightLove
Version:	1.6
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-MidnightLove
MidnightLove skin.

%description -n mplayer-skin-MidnightLove -l pl
Sk�rka MidnightLove.

%package -n mplayer-skin-WMP6
Summary:	WMP6 skin
Summary(pl):	Sk�rka WMP6
Version:	2.2
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skin-WindowsMediaPlayer6
Obsoletes:	mplayer-skins

%description -n mplayer-skin-WMP6
WMP6 skin.

%description -n mplayer-skin-WMP6 -l pl
Sk�rka WMP6.

%package -n mplayer-skin-avifile
Summary:	avifile skin
Summary(pl):	Sk�rka avifile
Version:	1.6
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-avifile
avifile skin.

%description -n mplayer-skin-avifile -l pl
Sk�rka avifile.

%package -n mplayer-skin-neutron
Summary:	neutron skin
Summary(pl):	Sk�rka neutron
Version:	1.5
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-neutron
neutron skin.

%description -n mplayer-skin-neutron -l pl
Sk�rka neutron.

%package -n mplayer-skin-phony
Summary:	phony skin
Summary(pl):	Sk�rka phony
Version:	1.1
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-phony
phony skin.

%description -n mplayer-skin-phony -l pl
Sk�rka phony.

%package -n mplayer-skin-plastic
Summary:	plastic skin
Summary(pl):	Sk�rka plastic
Version:	1.2
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-plastic
plastic skin.

%description -n mplayer-skin-plastic -l pl
Sk�rka plastic.

%package -n mplayer-skin-proton
Summary:	proton skin
Summary(pl):	Sk�rka proton
Version:	1.2
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-proton
proton skin.

%description -n mplayer-skin-proton -l pl
Sk�rka proton.

%package -n mplayer-skin-xanim
Summary:	xanim skin
Summary(pl):	Sk�rka xanim
Version:	1.6
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-xanim
xanim skin.

%description -n mplayer-skin-xanim -l pl
Sk�rka xanim.

%package -n mplayer-skin-xine-lcd
Summary:	xine-lcd skin
Summary(pl):	Sk�rka xine-lcd
Version:	1.2
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-xine-lcd
xine-lcd skin.

%description -n mplayer-skin-xine-lcd -l pl
Sk�rka xine-lcd.

%package -n mplayer-skin-mentalic
Summary:	mentalic skin
Summary(pl):	Sk�rka mentalic
Version:	1.2
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-mentalic
mentalic skin.

%description -n mplayer-skin-mentalic -l pl
Sk�rka mentalic.

%package -n mplayer-skin-AlienMind
Summary:	AlienMind skin
Summary(pl):	Sk�rka AlienMind
Version:	1.2
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-AlienMind
AlienMind skin.

%description -n mplayer-skin-AlienMind -l pl
Sk�rka AlienMind.

%package -n mplayer-skin-hwswskin
Summary:	hwswskin skin
Summary(pl):	Sk�rka hwswskin
Version:	1.1
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-hwswskin
hwswskin skin.

%description -n mplayer-skin-hwswskin -l pl
Sk�rka hwswskin.

%package -n mplayer-skin-XFce4
Summary:	XFce4 skin
Summary(pl):	Sk�rka XFce4
Version:	1.0
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-XFce4
XFce4 skin.

%description -n mplayer-skin-XFce4 -l pl
Sk�rka XFce4.

%package -n mplayer-skin-OSX-Brushed
Summary:	OSX-Brushed skin
Summary(pl):	Sk�rka OSX-Brushed
Version:	2.3
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-OSX-Brushed
OSX-Brushed skin.

%description -n mplayer-skin-OSX-Brushed -l pl
Sk�rka OSX-Brushed.

%package -n mplayer-skin-CornerMP
Summary:	CornerMP skin
Summary(pl):	Sk�rka CornerMP
Version:	1.2
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-CornerMP
CornerMP skin.

%description -n mplayer-skin-CornerMP -l pl
Sk�rka CornerMP.

%package -n mplayer-skin-CornerMP-aqua
Summary:	CornerMP-aqua skin
Summary(pl):	Sk�rka CornerMP-aqua
Version:	1.4
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-CornerMP-aqua
CornerMP-aqua skin.

%description -n mplayer-skin-CornerMP-aqua -l pl
Sk�rka CornerMP-aqua.

%package -n mplayer-skin-Plastik
Summary:	Plastik skin
Summary(pl):	Sk�rka Plastik
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-Plastik
Plastik skin.

%description -n mplayer-skin-Plastik -l pl
Sk�rka Plastik.

%package -n mplayer-skin-new-age
Summary:	new-age skin
Summary(pl):	Sk�rka new-age
Version:	1.0
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-new-age
new-age skin.

%description -n mplayer-skin-new-age -l pl
Sk�rka new-age.

%package -n mplayer-skin-Terminator3
Summary:	Terminator3 skin
Summary(pl):	Sk�rka Terminator3
Version:	1.1
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-Terminator3
Terminator3 skin.

%description -n mplayer-skin-Terminator3 -l pl
Sk�rka Terminator3.

%package -n mplayer-skin-OSX-Mod
Summary:	OSX-Mod skin
Summary(pl):	Sk�rka OSX-Mod
Version:	1.1
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-OSX-Mod
OSX-Mod skin.

%description -n mplayer-skin-OSX-Mod -l pl
Sk�rka OSX-Mod.

%package -n mplayer-skin-Industrial
Summary:	Industrial skin
Summary(pl):	Sk�rka Industrial
Version:	1.0
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-Industrial
Industrial skin.

%description -n mplayer-skin-Industrial -l pl
Sk�rka Industrial.

%package -n mplayer-skin-DVDPlayer
Summary:	DVDPlayer skin
Summary(pl):	Sk�rka DVDPlayer
Version:	1.1
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-DVDPlayer
DVDPlayer skin.

%description -n mplayer-skin-DVDPlayer -l pl
Sk�rka DVDPlayer.

%package -n mplayer-skin-Blue
Summary:	Blue skin
Summary(pl):	Sk�rka Blue
Version:	1.4
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-Blue
Blue skin (new default MPlayer skin).

%description -n mplayer-skin-Blue -l pl
Sk�rka Blue (obecnie domylna sk�rka MPlayera).

%package -n mplayer-skin-ultrafina
Summary:	ultrafina skin
Summary(pl):	Sk�rka ultrafina
Version:	1.1
Group:		X11/Applications/Multimedia
Requires:	gmplayer
Provides:	mplayer-skin
Obsoletes:	mplayer-skins

%description -n mplayer-skin-ultrafina
ultrafina skin (based on the XMMS ultrafina skin).

%description -n mplayer-skin-ultrafina -l pl
Sk�rka ultrafina (sk�rka wzorowana na sk�rce ultrafina do XMMS).

# NEW SKIN MARKER: PREAMBLE
%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_skindir}

bzip2 -dc %{SOURCE1} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE2} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE3} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE4} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE5} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE6} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE7} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE8} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE9} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE10} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE11} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE12} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE13} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE14} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE15} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE16} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE17} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
gzip -dc %{SOURCE18} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE19} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE20} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE21} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE22} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE23} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE24} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE25} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
bzip2 -dc %{SOURCE26} | tar -x -C $RPM_BUILD_ROOT%{_skindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
	ln -snf Blue %{_skindir}/default
fi

%post -n mplayer-skin-BlueHeart
if [ "$1" = 1 ]; then
	ln -snf BlueHeart %{_skindir}/default
fi

%post -n mplayer-skin-Cyrus
if [ "$1" = 1 ]; then
	ln -snf Cyrus %{_skindir}/default
fi

%post -n mplayer-skin-MidnightLove
if [ "$1" = 1 ]; then
	ln -snf MidnightLove %{_skindir}/default
fi

%post -n mplayer-skin-WMP6
if [ "$1" = 1 ]; then
	ln -snf WMP6 %{_skindir}/default
fi

%post -n mplayer-skin-avifile
if [ "$1" = 1 ]; then
	ln -snf avifile %{_skindir}/default
fi

%post -n mplayer-skin-neutron
if [ "$1" = 1 ]; then
	ln -snf neutron %{_skindir}/default
fi

%post -n mplayer-skin-phony
if [ "$1" = 1 ]; then
	ln -snf phony %{_skindir}/default
fi

%post -n mplayer-skin-plastic
if [ "$1" = 1 ]; then
	ln -snf plastic %{_skindir}/default
fi

%post -n mplayer-skin-proton
if [ "$1" = 1 ]; then
	ln -snf proton %{_skindir}/default
fi

%post -n mplayer-skin-xanim
if [ "$1" = 1 ]; then
	ln -snf xanim %{_skindir}/default
fi

%post -n mplayer-skin-xine-lcd
if [ "$1" = 1 ]; then
	ln -snf xine-lcd %{_skindir}/default
fi

%post -n mplayer-skin-mentalic
if [ "$1" = 1 ]; then
	ln -snf mentalic %{_skindir}/default
fi

%post -n mplayer-skin-AlienMind
if [ "$1" = 1 ]; then
	ln -snf AlienMind %{_skindir}/default
fi

%post -n mplayer-skin-hwswskin
if [ "$1" = 1 ]; then
	ln -snf hwswskin %{_skindir}/default
fi

%post -n mplayer-skin-XFce4
if [ "$1" = 1 ]; then
	ln -snf XFce4 %{_skindir}/default
fi

%post -n mplayer-skin-OSX-Brushed
if [ "$1" = 1 ]; then
	ln -snf OSX-Brushed %{_skindir}/default
fi

%post -n mplayer-skin-CornerMP
if [ "$1" = 1 ]; then
	ln -snf CornerMP %{_skindir}/default
fi

%post -n mplayer-skin-CornerMP-aqua
if [ "$1" = 1 ]; then
	ln -snf CornerMP-aqua %{_skindir}/default
fi

%post -n mplayer-skin-Plastik
if [ "$1" = 1 ]; then
	ln -snf Plastik %{_skindir}/default
fi

%post -n mplayer-skin-new-age
if [ "$1" = 1 ]; then
	ln -snf new-age %{_skindir}/default
fi

%post -n mplayer-skin-Terminator3
if [ "$1" = 1 ]; then
	ln -snf Terminator3 %{_skindir}/default
fi

%post -n mplayer-skin-OSX-Mod
if [ "$1" = 1 ]; then
	ln -snf OSX-Mod %{_skindir}/default
fi

%post -n mplayer-skin-Industrial
if [ "$1" = 1 ]; then
	ln -snf Industrial %{_skindir}/default
fi

%post -n mplayer-skin-DVDPlayer
if [ "$1" = 1 ]; then
	ln -snf DVDPlayer %{_skindir}/default
fi

%post -n mplayer-skin-Blue
if [ "$1" = 1 ]; then
	ln -snf Blue %{_skindir}/default
fi

%post -n mplayer-skin-ultrafina
if [ "$1" = 1 ]; then
	ln -snf ultrafina %{_skindir}/default
fi

# NEW SKIN MARKER: POST
%files
%defattr(644,root,root,755)
%{_skindir}/*

%files -n mplayer-skin-BlueHeart
%defattr(644,root,root,755)
%{_skindir}/BlueHeart

%files -n mplayer-skin-Cyrus
%defattr(644,root,root,755)
%{_skindir}/Cyrus

%files -n mplayer-skin-MidnightLove
%defattr(644,root,root,755)
%{_skindir}/MidnightLove

%files -n mplayer-skin-WMP6
%defattr(644,root,root,755)
%{_skindir}/WMP6

%files -n mplayer-skin-avifile
%defattr(644,root,root,755)
%{_skindir}/avifile

%files -n mplayer-skin-neutron
%defattr(644,root,root,755)
%{_skindir}/neutron

%files -n mplayer-skin-phony
%defattr(644,root,root,755)
%{_skindir}/phony

%files -n mplayer-skin-plastic
%defattr(644,root,root,755)
%{_skindir}/plastic

%files -n mplayer-skin-proton
%defattr(644,root,root,755)
%{_skindir}/proton

%files -n mplayer-skin-xanim
%defattr(644,root,root,755)
%{_skindir}/xanim

%files -n mplayer-skin-xine-lcd
%defattr(644,root,root,755)
%{_skindir}/xine-lcd

%files -n mplayer-skin-mentalic
%defattr(644,root,root,755)
%{_skindir}/mentalic

%files -n mplayer-skin-AlienMind
%defattr(644,root,root,755)
%{_skindir}/AlienMind

%files -n mplayer-skin-hwswskin
%defattr(644,root,root,755)
%{_skindir}/hwswskin

%files -n mplayer-skin-XFce4
%defattr(644,root,root,755)
%{_skindir}/XFce4

%files -n mplayer-skin-OSX-Brushed
%defattr(644,root,root,755)
%{_skindir}/OSX-Brushed

%files -n mplayer-skin-CornerMP
%defattr(644,root,root,755)
%{_skindir}/CornerMP

%files -n mplayer-skin-CornerMP-aqua
%defattr(644,root,root,755)
%{_skindir}/CornerMP-aqua

%files -n mplayer-skin-Plastik
%defattr(644,root,root,755)
%{_skindir}/Plastik

%files -n mplayer-skin-new-age
%defattr(644,root,root,755)
%{_skindir}/new-age

%files -n mplayer-skin-Terminator3
%defattr(644,root,root,755)
%{_skindir}/Terminator3

%files -n mplayer-skin-OSX-Mod
%defattr(644,root,root,755)
%{_skindir}/OSX-Mod

%files -n mplayer-skin-Industrial
%defattr(644,root,root,755)
%{_skindir}/Industrial

%files -n mplayer-skin-DVDPlayer
%defattr(644,root,root,755)
%{_skindir}/DVDPlayer

%files -n mplayer-skin-Blue
%defattr(644,root,root,755)
%{_skindir}/Blue

%files -n mplayer-skin-ultrafina
%defattr(644,root,root,755)
%{_skindir}/ultrafina

# NEW SKIN MARKER: FILES
