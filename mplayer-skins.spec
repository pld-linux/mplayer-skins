Summary:	MPlayer - skins
Summary(pl):	MPlayer - skóry
Name:		mplayer-skins
Version:	0.60
Release:	1
License:	distributable
Group:		X11/Applications/Multimedia
Source0:	ftp://mplayerhq.hu/MPlayer/Skin/BlueHeart.tar.bz2
Source1:	ftp://mplayerhq.hu/MPlayer/Skin/Cyrus.tar.bz2
Source2:	ftp://mplayerhq.hu/MPlayer/Skin/MidnightLove.tar.bz2
Source3:	ftp://mplayerhq.hu/MPlayer/Skin/WindowsMediaPlayer6.tar.bz2
Source4:	ftp://mplayerhq.hu/MPlayer/Skin/avifile.tar.bz2
Source5:	ftp://mplayerhq.hu/MPlayer/Skin/neutron.tar.bz2
Source6:	ftp://mplayerhq.hu/MPlayer/Skin/phony.tar.bz2
Source7:	ftp://mplayerhq.hu/MPlayer/Skin/plastic.tar.bz2
Source8:	ftp://mplayerhq.hu/MPlayer/Skin/proton.tar.bz2
Source9:	ftp://mplayerhq.hu/MPlayer/Skin/xanim.tar.bz2
Source10:	ftp://mplayerhq.hu/MPlayer/Skin/xine-lcd.tar.bz2
#Source11:	ftp://mplayerhq.hu/MPlayer/Skin/mentalic
# this one is broken
URL:		http://www.mplayerhq.hu/
Requires:	mplayer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/default-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_skindir	%{_prefix}/share/mplayer/Skin

%description
Addotional skins for MPlayer. Included are skins emulating look of
Windows Media Player, Avfile, Xine and many other.

%description -l pl
Dodtatkowe skórki dl MPlayera. W pakiecie znajudj± siê skórki udaj±ce
wygl±d Widows Media Player, Avifile, Xine i wiele innych.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_skindir}
%dir %{_skindir}/*
%{_skindir}/*/*.png
%{_skindir}/*/*.fnt
%{_skindir}/*/skin
