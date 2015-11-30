Name:           cmus
Version:        2.7.1
Release:        4%{?dist}
Summary:        Ncurses-Based Music Player

License:        GPLv2+
URL:            https://cmus.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz
  
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(flac)
BuildRequires:  faad2-devel
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libcue)
BuildRequires:  pkgconfig(libdiscid)
BuildRequires:  pkgconfig(libmikmod)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  libmpcdec-devel
BuildRequires:  libmp4v2-devel
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(wavpack)

%description
Small, fast and powerful console music player for Unix-like operating systems.
                                                                             
%prep
%setup -q

%build
./configure \
        prefix=%{_prefix} \
        libdir=%{_libdir} \
        CFLAGS="%{optflags}" \
        CONFIG_MIKMOD=y \
        CONFIG_VTX=n \
        CONFIG_ROAR=n \
        CONFIG_ARTS=n \
        CONFIG_SUN=n

%make_build V=2

%install
%make_install

mv %{buildroot}%{_docdir}/%{name}/examples .

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
install -pm 0644 contrib/%{name}.bash-completion %{buildroot}%{_sysconfdir}/bash_completion.d/

%files
%doc AUTHORS README.md examples
%license COPYING
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}.bash-completion
%{_bindir}/%{name}
%{_bindir}/%{name}-remote
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-remote.1.*
%{_mandir}/man7/%{name}-tutorial.7.*

%changelog
* Sat Oct 31 2015 Maxim Orlov <murmansksity@gmail.com> - 2.7.1-4.R
- move examples to right path

* Thu Oct 22 2015 Maxim Orlov <murmansksity@gmail.com> - 2.7.1-3.R
- add BR libcdio-paranoia-devel
- add BR libmikmod-devel
- add %%make_build
- remove make %%{?_smp_mflags} V=2
- cleanup spec

* Thu Sep 03 2015 Maxim Orlov <murmansksity@gmail.com> - 2.7.1-2.R
- remove BuildRequires: arts-devel

* Wed Sep 02 2015 Maxim Orlov <murmansksity@gmail.com> - 2.7.1-1.R
- Initial package.
