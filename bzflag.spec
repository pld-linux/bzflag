Summary:	multiplayer 3D tank battle game
Name:		bzflag
Version:	1.7e1
Release:	1
Copyright:	Chris Schoeneman 1993-1999
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/bzflag/%{name}_%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-paths.patch
Patch1:		%{name}-CFLAGS.patch
Patch2:		%{name}-printscore.patch
Patch3:		%{name}-lookups.patch
Icon:		bzflag.xpm
URL:		http://bzflag.org/
BuildRequires:	XFree86-OpenGL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
bzflag is a networked multiplayer 3D tank battle game, combining both
fast action and strategy. Free-for-all and capture-the-flag styles are
available.

%description -l pl
bzflag jest sieciow± gr± czo³gow± 3D, ³±cz±c± szybk± akcjê ze
strategi±. Graæ mo¿na w wolnym stylu lub metod± "zdob±d¼ flagê".

%prep
%setup -qn bzflag
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} linux # other, arch-dependent targets differ only in optymalization flags
%{__make} COPTFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O0 -g}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/bzflag,%{_applnkdir}/Games,%{_pixmapsdir},%{_mandir}/man6}

install bin/* $RPM_BUILD_ROOT%{_bindir}
install man/*.6s $RPM_BUILD_ROOT%{_mandir}/man6
install data/* $RPM_BUILD_ROOT%{_datadir}/bzflag
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install package/rpm/*.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README BUGS RELNOTES TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/bzflag
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
