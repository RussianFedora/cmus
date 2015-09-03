Name:           cmus
Version:        2.7.1
Release:        2%{?dist}
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
BuildRequires:  alsa-lib-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libdiscid-devel

%description
Small, fast and powerful console music player for Unix-like operating systems.
                                                                               
%prep
%setup -q

%build
./configure prefix=%{_prefix} bindir=%{_bindir} datadir=%{_datadir} \
  libdir=%{_libdir} mandir=%{_mandir} exampledir=%{_docdir}/%{name}/examples \
  CONFIG_ROAR=n CONFIG_ARTS=n CONFIG_SUN=n CFLAGS="%{optflags}"

make %{?_smp_mflags} V=2

%install
%make_install

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
install -pm 0644 contrib/%{name}.bash-completion %{buildroot}%{_sysconfdir}/bash_completion.d/

%files
%doc AUTHORS README.md
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-remote
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}.bash-completion
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-remote.1.*
%{_mandir}/man7/%{name}-tutorial.7.*
%{_libdir}/%{name}

%changelog
* Thu Sep 03 2015 Maxim Orlov <murmansksity@gmail.com> - 2.7.1-2.R
- remove BuildRequires: arts-devel

* Wed Sep 02 2015 Maxim Orlov <murmansksity@gmail.com> - 2.7.1-1.R
- Initial package.
