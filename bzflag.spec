Summary:	Multiplayer 3D tank battle game
Summary(pl):	Gra 3D dla wielu graczy - czo³gi
Name:		bzflag
Version:	1.10.2.20031223
Release:	0.1
License:	Chris Schoeneman 1993-1999
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	a4046c5af8882419deec97eea735ec96
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch4:		%{name}-etc_dir.patch
Icon:		bzflag.xpm
URL:		http://BZFlag.org/
BuildRequires:	OpenGL-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
bzflag is a networked multiplayer 3D tank battle game, combining both
fast action and strategy. Free-for-all and capture-the-flag styles are
available.

%description -l pl
bzflag jest sieciow± gr± czo³gow± 3D, ³±cz±c± szybk± akcjê ze
strategi±. Graæ mo¿na w wolnym stylu lub metod± "zdob±d¼ flagê".

%prep
%setup -q
#%patch4 -p1

%build

%{__aclocal}
%{__autoheader}
%{__automake} --add-missing
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/bzflag} \
	$RPM_BUILD_ROOT{%{_desktopdir}/Games,%{_pixmapsdir},%{_mandir}/man6}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README BUGS RELNOTES TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/bzflag
%{_desktopdir}/Games/*
%{_pixmapsdir}/*
