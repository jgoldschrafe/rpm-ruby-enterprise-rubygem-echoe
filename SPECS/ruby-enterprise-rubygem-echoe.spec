%define _prefix /opt/ruby-enterprise
%define _gem %{_prefix}/bin/gem
%define _ruby %{_prefix}/bin/ruby

# Generated from echoe-4.5.6.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{_ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{_ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname echoe
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A Rubygems packaging tool that provides Rake tasks for documentation, extension compiling, testing, and deployment
Name: ruby-enterprise-rubygem-%{gemname}
Version: 4.5.6
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://fauna.github.com/fauna/echoe/
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby-enterprise-rubygems
Requires: ruby-enterprise-rubygem(allison) >= 0
BuildRequires: ruby-enterprise-rubygems
BuildArch: noarch
Provides: ruby-enterprise-rubygem(%{gemname}) = %{version}

%description
A Rubygems packaging tool that provides Rake tasks for documentation,
extension compiling, testing, and deployment.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
%{_gem} install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/CHANGELOG
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README
%doc %{geminstdir}/lib/echoe.rb
%doc %{geminstdir}/lib/echoe/extensions.rb
%doc %{geminstdir}/lib/echoe/platform.rb
%doc %{geminstdir}/lib/echoe/rubygems.rb
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct  3 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 4.5.6-2.hhg
- Rebuild for Ruby Enterprise Edition

* Tue Apr 12 2011 Sergio Rubio <rubiojr@frameos.org> - 4.5.6-2
- remove rubyforge dep
- remove gemcutter dep

* Tue Apr 12 2011 Sergio Rubio <rubiojr@frameos.org> - 4.5.6-1
- Initial package
