Summary:	System log viewer for GNOME
Summary(pl.UTF-8):	Przeglądarka logów systemowych dla GNOME
Name:		gnome-system-log
Version:	3.4.0
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-system-log/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	c01c49c7bee58f58c865e35135d87021
URL:		http://live.gnome.org/GnomeUtils
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(find_lang) >= 1.35
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	zlib-devel
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.32.0
Requires:	hicolor-icon-theme
Provides:	gnome-utils-logview = 1:%{version}-%{release}
Obsoletes:	gnome-utils-logview < 1:3.3.2-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows to view system logs.

%description -l pl.UTF-8
Pozwala na przeglądanie logów systemowych.

%prep
%setup -q

%build
install -d m4
%{__intltoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS TODO
%attr(755,root,root) %{_bindir}/gnome-system-log
%{_desktopdir}/gnome-system-log.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_datadir}/GConf/gsettings/logview.convert
%{_datadir}/gnome-system-log
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-system-log.gschema.xml
%{_mandir}/man1/gnome-system-log.1*
