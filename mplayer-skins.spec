Summary:	MPlayer - skins
Summary(pl):	MPlayer - skóry
Name:		mplayer-skins
Version:	0.60
Release:	3
License:	distributable
Group:		X11/Applications/Multimedia
Source0:	ftp://mplayerhq.hu/MPlayer/Skin/BlueHeart-1.4.tar.bz2
# Source0-md5: abacf062eb9166cf287379deb5be8170
Source1:	ftp://mplayerhq.hu/MPlayer/Skin/Cyrus-1.0.tar.bz2
# Source1-md5: b4381b4bf77f89ef3d31e2a354af3ddc
Source2:	ftp://mplayerhq.hu/MPlayer/Skin/MidnightLove-1.5.tar.bz2
# Source2-md5: 8e7614b366d25622197997344149747c
Source3:	ftp://mplayerhq.hu/MPlayer/Skin/WindowsMediaPlayer6-1.2.tar.bz2
# Source3-md5: 6717e3f57e9c808777ce8cfc370d194e
Source4:	ftp://mplayerhq.hu/MPlayer/Skin/avifile-1.5.tar.bz2
# Source4-md5: a18d2282e5945243862fa765146c1b32
Source5:	ftp://mplayerhq.hu/MPlayer/Skin/neutron-1.4.tar.bz2
# Source5-md5: 6fcf7cee80805b8da1486337dbd81ef8
Source6:	ftp://mplayerhq.hu/MPlayer/Skin/phony-1.0.tar.bz2
# Source6-md5: c4e53b339b9ea986e2e9c5a2cf899584
Source7:	ftp://mplayerhq.hu/MPlayer/Skin/plastic-1.1.1.tar.bz2
# Source7-md5: e3fa0a19324631e4437dd992af17189c
Source8:	ftp://mplayerhq.hu/MPlayer/Skin/proton-1.1.tar.bz2
# Source8-md5: c59a504312e3b0eb363276a29ce715fe
Source9:	ftp://mplayerhq.hu/MPlayer/Skin/xanim-1.5.tar.bz2
# Source9-md5: 11c50f9eb970f08b4955bed6e3159d39
Source10:	ftp://mplayerhq.hu/MPlayer/Skin/xine-lcd-1.0.tar.bz2
# Source10-md5: 9e8a8ba86e46e714d1ef2e19d9a7e0cf
Source11:	ftp://mplayerhq.hu/MPlayer/Skin/mentalic-1.1.tar.bz2
# Source11-md5:	4eadeb691b25970116c8bfee42f856ec

URL:		http://www.mplayerhq.hu/
Requires:	mplayer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
bzip2 -dc %{SOURCE11} | tar -x -C $RPM_BUILD_ROOT%{_skindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_skindir}/*
