Summary:	Multiplayer 3D tank battle game
Summary(pl):	Gra 3D dla wielu graczy - czo³gi
Name:		bzflag
Version:	1.10.8.20041007
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	59d88fc8f8fe78bc6495e4c19c383323
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-etc_dir.patch
Patch1:		%{name}-nolibs.patch
Icon:		bzflag.xpm
URL:		http://BZFlag.org/
BuildRequires:	OpenGL-devel
BuildRequires:	adns-devel
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	OpenGL
Requires:	%{name}-server = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
bzflag is a networked multiplayer 3D tank battle game, combining both
fast action and strategy. Free-for-all and capture-the-flag styles are
available.

%description -l pl
bzflag jest sieciow± gr± czo³gow± 3D, ³±cz±c± szybk± akcjê ze
strategi±. Graæ mo¿na w wolnym stylu lub metod± "zdob±d¼ flagê".

%package server
Summary:	bzflag server and console utilities
Summary(pl):	Server bzflag i narzedzia konsolowe
Group:		X11/Applications/Games
Conflicts:	bzflag < 1.10.8.20041007-1

%description server
bzflag server and console utilities.

%description server -l pl
Server bzflag i narzedzia konsolowe.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure

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
%doc README BUGS RELNOTES TODO ChangeLog
%attr(755,root,root) %{_bindir}/bzflag
%{_mandir}/man6/bzflag.6.gz
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.wav
%{_datadir}/%{name}/*.png
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
%lang(kg) %{_datadir}/%{name}/l10n/%{name}_kg.po
%lang(nl) %{_datadir}/%{name}/l10n/%{name}_nl.po
%lang(pt) %{_datadir}/%{name}/l10n/%{name}_pt.po
%lang(sv) %{_datadir}/%{name}/l10n/%{name}_sv.po

%files server
%attr(755,root,root) %{_bindir}/bzadmin
%attr(755,root,root) %{_bindir}/bzfrelay
%attr(755,root,root) %{_bindir}/bzfs
%{_mandir}/man6/bzadmin.6.gz
%{_mandir}/man6/bzf[!l]*
%{_mandir}/man6/bzfls.6.gz
