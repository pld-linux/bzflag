# bzflag
# Copyright 1993-1999, Chris Schoeneman
#
# This package is free software;  you can redistribute it and/or
# modify it under the terms of the license found in the file
# named LICENSE that should have accompanied this file.
#
# THIS PACKAGE IS PROVIDED ``AS IS'' AND WITHOUT ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED
# WARRANTIES OF MERCHANTIBILITY AND FITNESS FOR A PARTICULAR PURPOSE.
Name:		bzflag
Version:	1.7c
Release:	3
Copyright:	Chris Schoeneman 1993-1999
Group:		X11/Games/Video
URL:		http://www.bigfoot.com/~bzflag
BuildRoot:	/var/tmp/bzflag
Summary:	multiplayer 3D tank battle game

%define BZFLAG_DIR /usr/local/bzflag
%define BZFLAG_BIN_DIR %{BZFLAG_DIR}/bin
%define BZFLAG_DATA_DIR %{BZFLAG_DIR}/data
%define BZFLAG_MAN_DIR /usr/local/man/man6

Source: bzflag-%{version}.src.tar.gz
Source1: bzflag
Patch0: bzflag-%{version}.patch
Patch1: bzflag-%{version}.patch2

%description
bzflag is a networked multiplayer 3D tank battle game, combining
both fast action and strategy.  Free-for-all and capture-the-flag
styles are available.

%prep
%setup -n bzflag%{version}
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
mkdir -p ${RPM_BUILD_ROOT}{%{BZFLAG_BIN_DIR},%{BZFLAG_DATA_DIR},%{BZFLAG_MAN_DIR},/usr/X11R6/bin}
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
%attr(444, root, root) /usr/local/bzflag/data/bbolt.rgb
%attr(444, root, root) /usr/local/bzflag/data/boom.wav
%attr(444, root, root) /usr/local/bzflag/data/boxwall.rgb
%attr(444, root, root) /usr/local/bzflag/data/caution.rgb
%attr(444, root, root) /usr/local/bzflag/data/clouds.rgb
%attr(444, root, root) /usr/local/bzflag/data/explode1.rgb
%attr(444, root, root) /usr/local/bzflag/data/explosion.wav
%attr(444, root, root) /usr/local/bzflag/data/fire.wav
%attr(444, root, root) /usr/local/bzflag/data/fixedbr.rgb
%attr(444, root, root) /usr/local/bzflag/data/fixedmr.rgb
%attr(444, root, root) /usr/local/bzflag/data/flag.rgb
%attr(444, root, root) /usr/local/bzflag/data/flag_alert.wav
%attr(444, root, root) /usr/local/bzflag/data/flag_drop.wav
%attr(444, root, root) /usr/local/bzflag/data/flag_grab.wav
%attr(444, root, root) /usr/local/bzflag/data/flag_lost.wav
%attr(444, root, root) /usr/local/bzflag/data/flag_won.wav
%attr(444, root, root) /usr/local/bzflag/data/flage.rgb
%attr(444, root, root) /usr/local/bzflag/data/gbolt.rgb
%attr(444, root, root) /usr/local/bzflag/data/ground.rgb
%attr(444, root, root) /usr/local/bzflag/data/helvbi.rgb
%attr(444, root, root) /usr/local/bzflag/data/helvbr.rgb
%attr(444, root, root) /usr/local/bzflag/data/laser.wav
%attr(444, root, root) /usr/local/bzflag/data/laser.rgb
%attr(444, root, root) /usr/local/bzflag/data/missile.rgb
%attr(444, root, root) /usr/local/bzflag/data/mountain.rgb
%attr(444, root, root) /usr/local/bzflag/data/panel.rgb
%attr(444, root, root) /usr/local/bzflag/data/pbolt.rgb
%attr(444, root, root) /usr/local/bzflag/data/pop.wav
%attr(444, root, root) /usr/local/bzflag/data/pyrwall.rgb
%attr(444, root, root) /usr/local/bzflag/data/rbolt.rgb
%attr(444, root, root) /usr/local/bzflag/data/ricochet.wav
%attr(444, root, root) /usr/local/bzflag/data/roof.rgb
%attr(444, root, root) /usr/local/bzflag/data/shock.wav
%attr(444, root, root) /usr/local/bzflag/data/teleport.wav
%attr(444, root, root) /usr/local/bzflag/data/timesbi.rgb
%attr(444, root, root) /usr/local/bzflag/data/timesbr.rgb
%attr(444, root, root) /usr/local/bzflag/data/title.rgb
%attr(444, root, root) /usr/local/bzflag/data/wall.rgb
%attr(444, root, root) /usr/local/bzflag/data/ybolt.rgb
%attr(444, root, root) /usr/local/man/man6/bzflag.6
%attr(444, root, root) /usr/local/man/man6/bzfs.6

%changelog
* Thu Sep  2 1999 Peter Hanecak <hanecak@megaloman.sk>
- updated with patch 2 from Jul 28 1999 (solaris sound support)

* Fri Jun 25 1999 Peter Hanecak <hanecak@megaloman.sk>
- changed original spec so building is possible with it
(%prep, %build, %install, %clean)
- %dir /usr/local/bzflag
