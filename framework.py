#-*-coding:utf8;-*-
#qpy:2
#qpy:console

print "This is console module"
<?xml version="1.0"?>
<configuration>

  <appSettings>
    <add key="aspnet:UseTaskFriendlySynchronizationContext" value="true" />
  </appSettings>
  <system.web>
    <compilation debug="true" strict="false" explicit="true" targetFramework="4.5" />
    <httpRuntime targetFramework="4.5"/>
  </system.web>
  <system.serviceModel>
    <behaviors>
      <endpointBehaviors>
        <behavior name="httpBehavior">
          <webHttp />
        </behavior>
      </endpointBehaviors>
      <serviceBehaviors>
        <behavior>

          <serviceMetadata httpGetEnabled="true" httpsGetEnabled="true"/>

          <serviceDebug includeExceptionDetailInFaults="false"/>
        </behavior>
      </serviceBehaviors>
    </behaviors>
    <services>
      <service name="WcfAndroid.Service1">
        <endpoint address=""
            behaviorConfiguration="httpBehavior"
            binding="webHttpBinding"
            contract="WcfAndroid.IService1" />

      </service>
    </services>
    <protocolMapping>
        <add binding="webHttpBinding" scheme="https" />
    </protocolMapping>    
    <serviceHostingEnvironment aspNetCompatibilityEnabled="true" multipleSiteBindingsEnabled="true" />
  </system.serviceModel>
  <system.webServer>
    <modules runAllManagedModulesForAllRequests="true"/>
     <directoryBrowse enabled="true"/>
  </system.webServer>

</configuration>