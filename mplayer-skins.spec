Summary:	MPlayer - skins
Summary(pl):	MPlayer - skóry
Name:		mplayer-skins
Version:	0.60
Release:	9
License:	distributable
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/BlueHeart-1.5.tar.bz2
# Source0-md5:	fc989a046d9859da45e35d527bfc9acf
Source1:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/Cyrus-1.2.tar.bz2
# Source1-md5:	33c9f70b1a609b90b786e88ba4e71bdc
Source2:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/MidnightLove-1.6.tar.bz2
# Source2-md5:	e0caeef812608903d6fb9d231dd1c921
Source3:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/WindowsMediaPlayer6-2.0.tar.bz2
# Source3-md5:	17792c2feebb615d4ffd3c175d362c5a
Source4:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/avifile-1.6.tar.bz2
# Source4-md5:	8461daefbcf31ca64446c39d16b3851f
Source5:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/neutron-1.5.tar.bz2
# Source5-md5:	8a58b45c54b96de539bbc433a94434b4
Source6:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/phony-1.1.tar.bz2
# Source6-md5:	50ad8b60117d006a3cae611d32759499
Source7:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/plastic-1.2.tar.bz2
# Source7-md5:	92a8c17fd85216ad382858babc9b508b
Source8:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/proton-1.2.tar.bz2
# Source8-md5:	54bc0241be0579792e439317d6fe853e
Source9:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/xanim-1.6.tar.bz2
# Source9-md5:	7523c0bdf6f59d26316e6cb5da4d3fb2
Source10:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/xine-lcd-1.2.tar.bz2
# Source10-md5:	8cd553b5650c82f99f554e1bb15df1e7
Source11:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/mentalic-1.2.tar.bz2
# Source11-md5:	2167a5c5a21ed058fd245c728b2b3221
Source12:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/AlienMind-1.2.tar.bz2
# Source12-md5:	76c42820c0965753e94b057e7a3e7e2c
Source13:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/hwswskin-1.1.tar.bz2
# Source13-md5:	8cf72e80b937f8f02883447dce2b33c0
Source14:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/XFce4-1.0.tar.bz2
# Source14-md5:	64f6d3ee6d0667b8d6870eb378cb30a2
Source15:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/OSX-Brushed-2.3.tar.bz2
# Source15-md5:	a9a0f5f567fb85189119b5ebd4ca1a33
Source16:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/CornerMP-1.2.tar.bz2
# Source16-md5:	dacdac178e7f5fa323ad4e7f00daa465
Source17:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/CornerMP-aqua-1.4.tar.bz2
# Source17-md5:	f040b8d9e343e74fe32e985f17042091
Source18:       http://download.freshmeat.net/themes/plastikmplayer/plastikmplayer-default.tar.gz
# Source18-md5:	2a168d8663ad6f017647ea88258fc978
Source19:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/new-age-1.0.tar.bz2
# Source19-md5:	9b127ddfb9771b6a561b00b3bfe762e3
Source20:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/Terminator3-1.1.tar.bz2
# Source20-md5:	d1fa5c487cdbdc8e80b123e2c2873425
Source21:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/OSX-Mod-1.1.tar.bz2
# Source21-md5:	922947f030c92ad8fb8a276b41dc39d6
Source22:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/Industrial-1.0.tar.bz2
# Source22-md5:	f63e03adc8756a8eb008a966ddf13817
Source23:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/DVDPlayer-1.1.tar.bz2
# Source23-md5:	f1ae6c17a970a1b5efeb73af3f4aaab0
Source24:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/Blue-1.4.tar.bz2
# Source24-md5:	031cfc6718f5d66b5af3e257cbc87158
Source25:	ftp://ftp1.mplayerhq.hu/MPlayer/Skin/ultrafina-1.1.tar.bz2
# Source25-md5:	403d61ff2d2cddbfd76f5d0269725b7f
URL:		http://www.mplayerhq.hu/
Requires:	mplayer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_skindir	%{_prefix}/share/mplayer/Skin

%description
Additional skins for MPlayer. Included are skins emulating look of
Windows Media Player, Avfile, Xine and many others.

%description -l pl
Dodatkowe skórki dla MPlayera. W pakiecie znajduj± siê skórki udaj±ce
wygl±d Widows Media Player, Avifile, Xine i wiele innych.

%package -n mplayer-skin-BlueHeart
Summary:	BlueHeart skin
Summary(pl):	Skórka BlueHeart
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-BlueHeart
BlueHeart skin.

%description -n mplayer-skin-BlueHeart -l pl
Skórka BlueHeart.

%package -n mplayer-skin-Cyrus
Summary:	Cyrus skin
Summary(pl):	Skórka Cyrus
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-Cyrus
Cyrus skin.

%description -n mplayer-skin-Cyrus -l pl
Skórka Cyrus.

%package -n mplayer-skin-MidnightLove
Summary:	MidnightLove skin
Summary(pl):	Skórka MidnightLove
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-MidnightLove
MidnightLove skin.

%description -n mplayer-skin-MidnightLove -l pl
Skórka MidnightLove.

%package -n mplayer-skin-WindowsMediaPlayer6
Summary:	WindowsMediaPlayer6 skin
Summary(pl):	Skórka WindowsMediaPlayer6
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-WindowsMediaPlayer6
WindowsMediaPlayer6 skin.

%description -n mplayer-skin-WindowsMediaPlayer6 -l pl
Skórka WindowsMediaPlayer6.

%package -n mplayer-skin-avifile
Summary:	avifile skin
Summary(pl):	Skórka avifile
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-avifile
avifile skin.

%description -n mplayer-skin-avifile -l pl
Skórka avifile.

%package -n mplayer-skin-phony
Summary:	phony skin
Summary(pl):	Skórka phony
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-phony
phony skin.

%description -n mplayer-skin-phony -l pl
Skórka phony.

%package -n mplayer-skin-plastic
Summary:	plastic skin
Summary(pl):	Skórka plastic
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-plastic
plastic skin.

%description -n mplayer-skin-plastic -l pl
Skórka plastic.

%package -n mplayer-skin-proton
Summary:	proton skin
Summary(pl):	Skórka proton
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-proton
proton skin.

%description -n mplayer-skin-proton -l pl
Skórka proton.

%package -n mplayer-skin-xanim
Summary:	xanim skin
Summary(pl):	Skórka xanim
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-xanim
xanim skin.

%description -n mplayer-skin-xanim -l pl
Skórka xanim.

%package -n mplayer-skin-xine-lcd
Summary:	xine-lcd skin
Summary(pl):	Skórka xine-lcd
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-xine-lcd
xine-lcd skin.

%description -n mplayer-skin-xine-lcd -l pl
Skórka xine-lcd.

%package -n mplayer-skin-mentalic
Summary:	mentalic skin
Summary(pl):	Skórka mentalic
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-mentalic
mentalic skin.

%description -n mplayer-skin-mentalic -l pl
Skórka mentalic.

%package -n mplayer-skin-AlienMind
Summary:	AlienMind skin
Summary(pl):	Skórka AlienMind
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-AlienMind
AlienMind skin.

%description -n mplayer-skin-AlienMind -l pl
Skórka AlienMind.

%package -n mplayer-skin-hwswskin
Summary:	hwswskin skin
Summary(pl):	Skórka hwswskin
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-hwswskin
hwswskin skin.

%description -n mplayer-skin-hwswskin -l pl
Skórka hwswskin.

%package -n mplayer-skin-XFce4
Summary:	XFce4 skin
Summary(pl):	Skórka XFce4
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-XFce4
XFce4 skin.

%description -n mplayer-skin-XFce4 -l pl
Skórka XFce4.

%package -n mplayer-skin-OSX-Brushed
Summary:	OSX-Brushed skin
Summary(pl):	Skórka OSX-Brushed
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-OSX-Brushed
OSX-Brushed skin.

%description -n mplayer-skin-OSX-Brushed -l pl
Skórka OSX-Brushed.

%package -n mplayer-skin-CornerMP
Summary:	CornerMP skin
Summary(pl):	Skórka CornerMP
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-CornerMP
CornerMP skin.

%description -n mplayer-skin-CornerMP -l pl
Skórka CornerMP.

%package -n mplayer-skin-CornerMP-aqua
Summary:	CornerMP-aqua skin
Summary(pl):	Skórka CornerMP-aqua
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-CornerMP-aqua
CornerMP-aqua skin.

%description -n mplayer-skin-CornerMP-aqua -l pl
Skórka CornerMP-aqua.

%package -n mplayer-skin-Plastik
Summary:	Plastik skin
Summary(pl):	Skórka Plastik
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-Plastik
Plastik skin.

%description -n mplayer-skin-Plastik -l pl
Skórka Plastik.

%package -n mplayer-skin-new-age
Summary:	new-age skin
Summary(pl):	Skórka new-age
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-new-age
new-age skin.

%description -n mplayer-skin-new-age -l pl
Skórka new-age.

%package -n mplayer-skin-Terminator3
Summary:	Terminator3 skin
Summary(pl):	Skórka Terminator3
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-Terminator3
Terminator3 skin.

%description -n mplayer-skin-Terminator3 -l pl
Skórka Terminator3.

%package -n mplayer-skin-OSX-Mod
Summary:	OSX-Mod skin
Summary(pl):	Skórka OSX-Mod
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-OSX-Mod
OSX-Mod skin.

%description -n mplayer-skin-OSX-Mod -l pl
Skórka OSX-Mod.

%package -n mplayer-skin-Industrial
Summary:	Industrial skin
Summary(pl):	Skórka Industrial
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-Industrial
Industrial skin.

%description -n mplayer-skin-Industrial -l pl
Skórka Industrial.

%package -n mplayer-skin-DVDPlayer
Summary:	DVDPlayer skin
Summary(pl):	Skórka DVDPlayer
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-DVDPlayer
DVDPlayer skin.

%description -n mplayer-skin-DVDPlayer -l pl
Skórka DVDPlayer.

%package -n mplayer-skin-Blue
Summary:	Blue skin
Summary(pl):	Skórka Blue
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-Blue
Blue skin (new default MPlayer skin).

%description -n mplayer-skin-Blue -l pl
Skórka Blue (obecnie domylna skórka MPlayera).

%package -n mplayer-skin-ultrafina
Summary:	ultrafina skin
Summary(pl):	Skórka ultrafina
Group:		X11/Applications/Multimedia

%description -n mplayer-skin-ultrafina
ultrafina skin (based on the XMMS ultrafina skin).

%description -n mplayer-skin-ultrafina -l pl
Skórka ultrafina (skórka wzorowana na skórce ultrafina do XMMS).

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_skindir}

bzip2 -dc %{SOURCE0} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
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

%clean
rm -rf $RPM_BUILD_ROOT

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

%files -n mplayer-skin-WindowsMediaPlayer6
%defattr(644,root,root,755)
%{_skindir}/WindowsMediaPlayer6

%files -n mplayer-skin-avifile
%defattr(644,root,root,755)
%{_skindir}/avifile

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
