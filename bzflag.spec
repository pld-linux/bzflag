Summary:	Multiplayer 3D tank battle game
Summary(pl):	Gra 3D dla wielu graczy - czo³gi
Name:		bzflag
Version:	1.10.6.20040515
Release:	3
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	8e3e5fbef3cfa21079eb06269e6b3d8b
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-etc_dir.patch
Icon:		bzflag.xpm
URL:		http://BZFlag.org/
BuildRequires:	OpenGL-devel
BuildRequires:	adns-devel
BuildRequires:	autoconf
BuildRequires:	automake
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
#%patch0 -p1

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

# to be changed after adding Categories
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
#install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README BUGS RELNOTES TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/bzflag
%{_desktopdir}/*.desktop
#%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
