Name:           cmus
Version:        2.7.1
Release:        3%{?dist}
Summary:        Ncurses-Based Music Player

License:        GPLv2+
URL:            https://cmus.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz
  
BuildRequires:  ncurses-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  libao-devel
BuildRequires:  libcddb-devel
BuildRequires:  opusfile-devel
BuildRequires:  libcue-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  libvorbis-devel
BuildRequires:  flac-devel
BuildRequires:  faad2-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libmad-devel
BuildRequires:  libmp4v2-devel
BuildRequires:  wavpack-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libdiscid-devel
BuildRequires:  libcdio-paranoia-devel
BuildRequires:  libmikmod-devel

%description
Small, fast and powerful console music player for Unix-like operating systems.
                                                                               
%prep
%setup -q

%build
./configure \
        prefix=%{_prefix} \
        libdir=%{_libdir} \
        CONFIG_MIKMOD=y \
        CONFIG_VTX=n \
        CONFIG_ROAR=n \
        CONFIG_ARTS=n \
        CONFIG_SUN=n

%make_build

%install
%make_install

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
install -pm 0644 contrib/%{name}.bash-completion %{buildroot}%{_sysconfdir}/bash_completion.d/

%files
%doc AUTHORS README.md
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
* Thu Oct 22 2015 Maxim Orlov <murmansksity@gmail.com> - 2.7.1-3.R
- add BR libcdio-paranoia-devel
- add BR libmikmod-devel
- add %make_build
- remove make %{?_smp_mflags} V=2
- cleanup spec

* Thu Sep 03 2015 Maxim Orlov <murmansksity@gmail.com> - 2.7.1-2.R
- remove BuildRequires: arts-devel

* Wed Sep 02 2015 Maxim Orlov <murmansksity@gmail.com> - 2.7.1-1.R
- Initial package.
