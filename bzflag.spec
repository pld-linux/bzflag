Summary:	Multiplayer 3D tank battle game
Summary(pl):	Gra 3D dla wielu graczy - czo�gi
Name:		bzflag
Version:	1.7e6
Release:	1
License:	Chris Schoeneman 1993-1999
Group:		X11/Applications/Games
Source0:	ftp://ftp1.sourceforge.net/pub/sourceforge/bzflag/%{name}-%{version}.tgz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-paths.patch
Patch1:		%{name}-CFLAGS.patch
Patch2:		%{name}-printscore.patch
Patch3:		%{name}-lookups.patch
Icon:		bzflag.xpm
URL:		http://BZFlag.org/
BuildRequires:	OpenGL-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
bzflag is a networked multiplayer 3D tank battle game, combining both
fast action and strategy. Free-for-all and capture-the-flag styles are
available.

%description -l pl
bzflag jest sieciow� gr� czo�gow� 3D, ��cz�c� szybk� akcj� ze
strategi�. Gra� mo�na w wolnym stylu lub metod� "zdob�d� flag�".

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} linux # other, arch-dependent targets differ only in optymalization flags
%{__make} COPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/bzflag} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Games,%{_pixmapsdir},%{_mandir}/man6}

install bin/* $RPM_BUILD_ROOT%{_bindir}
install man/*.6s $RPM_BUILD_ROOT%{_mandir}/man6
install data/* $RPM_BUILD_ROOT%{_datadir}/bzflag
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README BUGS RELNOTES TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/bzflag
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
