Summary:	MPlayer - skins
Summary(pl):	MPlayer - skóry
Name:		mplayer-skins
Version:	0.60
Release:	2
License:	distributable
Group:		X11/Applications/Multimedia
Source0:	ftp://mplayerhq.hu/MPlayer/Skin/BlueHeart.tar.bz2
# Source0-md5: abacf062eb9166cf287379deb5be8170
Source1:	ftp://mplayerhq.hu/MPlayer/Skin/Cyrus.tar.bz2
# Source1-md5: d5e3c1ffa8536f15fadaa882609ff206
Source2:	ftp://mplayerhq.hu/MPlayer/Skin/MidnightLove.tar.bz2
# Source2-md5: f86d12bfdb9ecb4ec7db8fdac871f3dd
Source3:	ftp://mplayerhq.hu/MPlayer/Skin/WindowsMediaPlayer6.tar.bz2
# Source3-md5: d0c96a2f45c9df2d184d771fba353f77
Source4:	ftp://mplayerhq.hu/MPlayer/Skin/avifile.tar.bz2
# Source4-md5: f17c26b226c993268b0d938472312b14
Source5:	ftp://mplayerhq.hu/MPlayer/Skin/neutron.tar.bz2
# Source5-md5: 269764e6e3d7e9d94587b798f5e6b8cc
Source6:	ftp://mplayerhq.hu/MPlayer/Skin/phony.tar.bz2
# Source6-md5: ab75db8550c89192b2250e307b1531c0
Source7:	ftp://mplayerhq.hu/MPlayer/Skin/plastic.tar.bz2
# Source7-md5: f7f7b4b7b6db3a3502613ab8f5c1c79d
Source8:	ftp://mplayerhq.hu/MPlayer/Skin/proton.tar.bz2
# Source8-md5: 5101f39447089fbcf15423e15c6cf8fc
Source9:	ftp://mplayerhq.hu/MPlayer/Skin/xanim.tar.bz2
# Source9-md5: c3fb71d022c3f48b8b02247ed892c501
Source10:	ftp://mplayerhq.hu/MPlayer/Skin/xine-lcd.tar.bz2
# Source10-md5: c737868f8e4ad4b68bff0e903c84a10a
#Source11:	ftp://mplayerhq.hu/MPlayer/Skin/mentalic
# this one is broken
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_skindir}/*
