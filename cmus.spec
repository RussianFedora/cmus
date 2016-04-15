Name:           cmus
Version:        2.7.1
Release:        5%{?dist}
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
        bindir=%{_bindir} \
        datadir=%{_datadir} \
        libdir=%{_libdir} \
        mandir=%{_mandir} \
        exampledir=%{_docdir}/%{name}/examples \
        CFLAGS="%{optflags}" \
        CONFIG_AAC=y \
        CONFIG_ALSA=y \
        CONFIG_AO=y \
        CONFIG_ARTS=n \
        CONFIG_CDDB=y \
        CONFIG_CDIO=y \
        CONFIG_CUE=y \
        CONFIG_COREAUDIO=n \
        CONFIG_DISCID=y \
        CONFIG_FFMPEG=y \
        CONFIG_FLAC=y \
        CONFIG_JACK=y \
        CONFIG_MAD=y \
        CONFIG_MIKMOD=y \
        CONFIG_MODPLUG=y \
        CONFIG_MPC=y \
        CONFIG_MP4=y \
        CONFIG_OPUS=y \
        CONFIG_OSS=y \
        CONFIG_PULSE=y \
        CONFIG_ROAR=n \
        CONFIG_SAMPLERATE=y \
        CONFIG_SNDIO=n \
        CONFIG_SUN=n \
        CONFIG_TREMOR=n \
        CONFIG_VORBIS=y \
        CONFIG_VTX=n \
        CONFIG_WAV=y \
        CONFIG_WAVPACK=y \
        CONFIG_WAVEOUT=n

%make_build V=2

%install
%make_install

mv %{buildroot}%{_docdir}/%{name}/examples .

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
install -pm 0644 contrib/%{name}.bash-completion %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}

%files
%doc AUTHORS README.md examples
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-remote
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-remote.1.*
%{_mandir}/man7/%{name}-tutorial.7.*
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}

%changelog
* Mon Nov 30 2015 Maxim Orlov <murmansksity@gmail.com> - 2.7.1-5.R
- add V=2 (Make the build verbose)
- use pkgconfig for BuildRequires
- use proper CFLAGS

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
