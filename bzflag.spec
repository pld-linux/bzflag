Summary:	multiplayer 3D tank battle game
Name:		bzflag
Version:	1.7c
Release:	3
Copyright:	Chris Schoeneman 1993-1999
Group:		X11/Games/Video
Source:		bzflag-%{version}.src.tar.gz
Source1:	bzflag
Patch0:		bzflag-%{version}.patch
Patch1:		bzflag-%{version}.patch2
URL:		http://www.bigfoot.com/~bzflag/
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
bzflag is a networked multiplayer 3D tank battle game, combining both fast
action and strategy. Free-for-all and capture-the-flag styles are
available.

%description -l pl
bzflag jest sieciow± gr± czo³gow± 3D, ³±cz±c± szybk± akcjê ze strategi±. 
Graæ mo¿na w wolnym stylu lub metod± "zdob±d¼ flagê".

%prep
%setup -q -n bzflag%{version}
%patch0 -p1
%patch1 -p1

%build
%ifarch i386
make linux-i386
%else
%ifarch ppc
make linux-ppc
%else
make linux
%endif
%endif
make all

%install
install -d ${RPM_BUILD_ROOT}{%{BZFLAG_BIN_DIR},%{BZFLAG_DATA_DIR},%{BZFLAG_MAN_DIR},/usr/X11R6/bin}
cp ${RPM_BUILD_DIR}/bzflag%{version}/bin/bzflag ${RPM_BUILD_ROOT}/%{BZFLAG_BIN_DIR}/bzflag.real
cp ${RPM_BUILD_DIR}/bzflag%{version}/bin/bzfs ${RPM_BUILD_ROOT}/%{BZFLAG_BIN_DIR}/bzfs
cp ${RPM_SOURCE_DIR}/bzflag ${RPM_BUILD_ROOT}/%{BZFLAG_BIN_DIR}/bzflag

cp ${RPM_BUILD_DIR}/bzflag%{version}/data/*.wav ${RPM_BUILD_ROOT}/%{BZFLAG_DATA_DIR}
cp ${RPM_BUILD_DIR}/bzflag%{version}/data/*.rgb ${RPM_BUILD_ROOT}/%{BZFLAG_DATA_DIR}

cp ${RPM_BUILD_DIR}/bzflag%{version}/man/bzflag.6 ${RPM_BUILD_ROOT}/%{BZFLAG_MAN_DIR}
cp ${RPM_BUILD_DIR}/bzflag%{version}/man/bzfs.6 ${RPM_BUILD_ROOT}/%{BZFLAG_MAN_DIR}

cd $RPM_BUILD_ROOT/usr/X11R6/bin
ln -s ../../local/bzflag/bin/bzflag

%clean
rm -rf $RPM_BUILD_ROOT

#
# note -- bzflag must be setuid root to use 3Dfx drivers
#
%files
%dir /usr/local/bzflag
%attr(-, root, root) %doc README
%attr(-, root, root) %doc LICENSE
#%attr(04755, root, root) /usr/local/bzflag/bin/bzflag.real
%attr(755, root, root) /usr/local/bzflag/bin/bzflag.real
%attr(755, root, root) /usr/local/bzflag/bin/bzflag
%attr(755, root, root) /usr/local/bzflag/bin/bzfs
%attr(755, root, root) /usr/X11R6/bin/bzflag
/usr/local/bzflag/data/bbolt.rgb
/usr/local/bzflag/data/boom.wav
/usr/local/bzflag/data/boxwall.rgb
/usr/local/bzflag/data/caution.rgb
/usr/local/bzflag/data/clouds.rgb
/usr/local/bzflag/data/explode1.rgb
/usr/local/bzflag/data/explosion.wav
/usr/local/bzflag/data/fire.wav
/usr/local/bzflag/data/fixedbr.rgb
/usr/local/bzflag/data/fixedmr.rgb
/usr/local/bzflag/data/flag.rgb
/usr/local/bzflag/data/flag_alert.wav
/usr/local/bzflag/data/flag_drop.wav
/usr/local/bzflag/data/flag_grab.wav
/usr/local/bzflag/data/flag_lost.wav
/usr/local/bzflag/data/flag_won.wav
/usr/local/bzflag/data/flage.rgb
/usr/local/bzflag/data/gbolt.rgb
/usr/local/bzflag/data/ground.rgb
/usr/local/bzflag/data/helvbi.rgb
/usr/local/bzflag/data/helvbr.rgb
/usr/local/bzflag/data/laser.wav
/usr/local/bzflag/data/laser.rgb
/usr/local/bzflag/data/missile.rgb
/usr/local/bzflag/data/mountain.rgb
/usr/local/bzflag/data/panel.rgb
/usr/local/bzflag/data/pbolt.rgb
/usr/local/bzflag/data/pop.wav
/usr/local/bzflag/data/pyrwall.rgb
/usr/local/bzflag/data/rbolt.rgb
/usr/local/bzflag/data/ricochet.wav
/usr/local/bzflag/data/roof.rgb
/usr/local/bzflag/data/shock.wav
/usr/local/bzflag/data/teleport.wav
/usr/local/bzflag/data/timesbi.rgb
/usr/local/bzflag/data/timesbr.rgb
/usr/local/bzflag/data/title.rgb
/usr/local/bzflag/data/wall.rgb
/usr/local/bzflag/data/ybolt.rgb
/usr/local/man/man6/bzflag.6
/usr/local/man/man6/bzfs.6
