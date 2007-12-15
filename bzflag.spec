# TODO:
#  - some python plugin can be built, but it's hardly disabled (why ?)
#  - there's lot of stuff in misc directory, some of them interesting
#    (to be compiled, moved to doc, or something else)
#  - bzfsAPI.h and other is marked ad noinst_HEADER, maybe in future it will
#    be installed too, to allow compiling plugins externall
#
Summary:	Multiplayer 3D tank battle game
Summary(pl.UTF-8):	Gra 3D dla wielu graczy - czołgi
Name:		bzflag
Version:	2.0.10
Release:	1
License:	LGPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/bzflag/%{name}-%{version}.tar.bz2
# Source0-md5:	64993b181e72ea713f813d0a78576b70
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-etc_dir.patch
Patch1:		%{name}-nolibs.patch
URL:		http://BZFlag.org/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	c-ares-devel
BuildRequires:	curl-devel >= 7.9.5
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
bzflag is a networked multiplayer 3D tank battle game, combining both
fast action and strategy. Free-for-all and capture-the-flag styles are
available.

%description -l pl.UTF-8
bzflag jest sieciową grą czołgową 3D, łączącą szybką akcję ze
strategią. Grać można w wolnym stylu lub metodą "zdobądź flagę".

%package server
Summary:	bzflag server and console utilities
Summary(pl.UTF-8):	Server bzflag i narzędzia konsolowe
Group:		X11/Applications/Games
Conflicts:	bzflag < 1.10.8.20041007-1

%description server
bzflag server and console utilities.

%description server -l pl.UTF-8
Server bzflag i narzędzia konsolowe.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1

:> m4/mkdirp.m4
:> m4/sdl.m4

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
CPPFLAGS="%{rpmcflags} -I/usr/include/ncurses"
export CFLAGS CPPFLAGS
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-threads	\
	--enable-plugins	\
	--enable-bzadmin	\
	--disable-timebomb	\
	--disable-sdltest	\
	--enable-client		\
	--enable-robots		\
	--enable-snapping

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/bzflag} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_mandir}/man6}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README README.Linux BUGS TODO ChangeLog
%attr(755,root,root) %{_bindir}/bzflag
%{_mandir}/man6/bzflag.6*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.xpm
%{_datadir}/%{name}/*.wav
%{_datadir}/%{name}/*.png
%dir %{_datadir}/%{name}/fonts
%{_datadir}/%{name}/fonts/*
%dir %{_datadir}/%{name}/l10n
%{_datadir}/%{name}/l10n/%{name}_xx.po
%{_datadir}/%{name}/l10n/ISO-639-2_values_8bits.txt
%lang(cs) %{_datadir}/%{name}/l10n/%{name}_cs_CZ.po
%lang(da) %{_datadir}/%{name}/l10n/%{name}_da.po
%lang(de) %{_datadir}/%{name}/l10n/%{name}_de.po
%lang(en) %{_datadir}/%{name}/l10n/%{name}_en_US_l33t.po
%lang(en) %{_datadir}/%{name}/l10n/%{name}_en_US_redneck.po
%lang(es) %{_datadir}/%{name}/l10n/%{name}_es.po
%lang(fr) %{_datadir}/%{name}/l10n/%{name}_fr.po
%lang(it) %{_datadir}/%{name}/l10n/%{name}_it.po
%lang(tlh) %{_datadir}/%{name}/l10n/%{name}_kg.po
%lang(lt) %{_datadir}/%{name}/l10n/%{name}_lt.po
%lang(nl) %{_datadir}/%{name}/l10n/%{name}_nl.po
%lang(pt) %{_datadir}/%{name}/l10n/%{name}_pt.po
%lang(sv) %{_datadir}/%{name}/l10n/%{name}_sv.po
#%attr(755,root,root) %{_libdir}/*.so

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bzadmin
%attr(755,root,root) %{_bindir}/bzfs
%{_mandir}/man5/bzw.5*
%{_mandir}/man6/bzadmin.6*
%{_mandir}/man6/bzf[!l]*
