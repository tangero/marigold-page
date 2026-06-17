---
slug: "iua"
url: "/mobilnisite/slovnik/iua/"
type: "slovnik"
title: "IUA – IMS User Agent"
date: 2025-01-01
abbr: "IUA"
fullName: "IMS User Agent"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/iua/"
summary: "IMS User Agent (IUA) je funkční entita v uživatelském zařízení (UE) nebo terminálu, která funguje jako klientský koncový bod pro služby založené na IMS. Zajišťuje SIP registraci, navazování relací a s"
---

IUA je funkční entita v uživatelském zařízení, která slouží jako klientský koncový bod pro služby IMS a zajišťuje SIP registraci, navazování relací a servisní logiku.

## Popis

IMS User Agent (IUA) je klíčová klientská aplikační komponenta definovaná v architektuře 3GPP IP Multimedia Subsystem (IMS). Nachází se v uživatelském zařízení (UE) a jedná se o softwarovou entitu, která implementuje funkčnost IMS klienta a přímo komunikuje s jádrovou sítí IMS za účelem registrace, navazování a správy multimediálních relací. IUA je v zásadě Session Initiation Protocol (SIP) User Agent, jak je definován v [IETF](/mobilnisite/slovnik/ietf/) RFC 3261, ale je rozšířen a profilován 3GPP pro provoz v rámci specifických omezení a servisních prostředí mobilní sítě, včetně požadavků na autentizaci, zabezpečení a propojení se službami s přepojováním okruhů.

Z architektonického hlediska se IUA nachází v aplikační vrstvě nebo modemovém zásobníku UE. Mezi jeho klíčové komponenty patří SIP zásobník pro zpracování protokolu, modul Session Description Protocol (SDP) pro vyjednávání médií a implementace specifických 3GPP rozšíření a procedur SIP. Rozhraní má ke spodním vrstvám UE (např. ke 3GPP zásobníku protokolů pro navazování IP konektivity přes LTE nebo 5G) a k ostatním aplikacím v UE, které vyžadují služby IMS (např. aplikace pro vytáčení). Hlavními provozními rolemi IUA jsou registrace a řízení relací. Při registraci do IMS odešle IUA požadavek SIP REGISTER k funkci Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)), čímž zahájí proces IMS Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)). Pro navázání relace, například při uskutečnění VoLTE hovoru, IUA vygeneruje požadavek SIP INVITE s nabídkou SDP popisující požadované médium (např. [AMR-WB](/mobilnisite/slovnik/amr-wb/) audio), a poté zpracovává odpovědi SIP a odpovědi SDP od vzdálené strany.

Jak to funguje, zahrnuje podrobnou sekvenci SIP zpráv. Po zapnutí a připojení k paketové datové síti IUA zjistí adresu P-CSCF (pomocí [DHCP](/mobilnisite/slovnik/dhcp/) nebo ze sítě) a provede SIP registraci, která autentizuje uživatele a vytvoří bezpečnostní asociaci. Po registraci může iniciovat nebo přijímat relace. IUA implementuje specifické funkce 3GPP, jako je zpracování síťově iniciovaného odregistrování/nové autentizace, podpora nouzových relací a procedury ICS (IMS Centralized Services). V architektuře ICS (podrobně v 3GPP TS 23.292) hraje IUA klíčovou roli při ukotvení [CS](/mobilnisite/slovnik/cs/) hlasového hovoru UE přes jádro IMS, funguje jako SIP koncový bod, který komunikuje s [MSC](/mobilnisite/slovnik/msc/) Serverem rozšířeným pro ICS (eMSC), aby poskytl jednotnou servisní zkušenost.

## K čemu slouží

IMS User Agent existuje proto, aby umožnil uživatelskému zařízení přístup k bohatým, IP-based multimediálním službám poskytovaným jádrovou sítí IMS. Před IMS a IUA byl mobilní hlas primárně přepojován okruhy a pokročilé služby jako videohovory, rozšířené zasílání zpráv a kombinování služeb bylo obtížné standardizovat a nasadit. IUA poskytuje standardizovaný, interoperabilní klientský koncový bod, který řeší problém, jak různorodá řada typů UE (telefony, tablety, IoT zařízení) od různých výrobců může konzistentně přistupovat ke stejným službám IMS.

Jeho vytvoření bylo motivováno přechodem průmyslu k plně IP sítím. Architektura IMS byla navržena tak, aby oddělila služby od přístupové sítě, ale to vyžadovalo sofistikovaného klienta v zařízení, který by zvládal signalizaci SIP. IUA standardizuje toto chování klienta a zajišťuje, že funkce na úrovni sítě, jako je kvalita služby (QoS), nouzové hovory a zákonné odposlechy, fungují spolehlivě na všech kompatibilních zařízeních. Konkrétně v kontextu ICS zavedeného ve verzi 8 řeší IUA problém kontinuity služeb a konzistence služeb pro uživatele s UE, která podporují jak [CS](/mobilnisite/slovnik/cs/) přístup, tak IMS. Umožňuje síti centralizovat řízení služeb v jádru IMS i pro hovory využívající CS radiový přístup, což umožňuje funkce jako simultánní hlas a data a jednotnou schránku hlasové pošty, a řeší tak omezení tradičního uzavřeného doménového prostředí CS služeb. IUA je tedy nezbytným prvkem, který uvádí vizi služeb IMS v život na koncovém uživatelském zařízení.

## Klíčové vlastnosti

- Implementuje 3GPP profilované protokoly SIP a SDP pro signalizaci IMS.
- Provádí registraci a autentizaci do IMS pomocí IMS AKA.
- Iniciuje a ukončuje multimediální relace (např. hlas, video) pomocí SIP INVITE, BYE.
- Podporuje procedury ICS pro ukotvení CS hovorů přes jádro IMS za účelem konzistence služeb.
- Zpracovává síťově iniciované procedury, jako je nová autentizace a odregistrování.
- Spravuje vyjednávání médií a výběr kodeků na základě možností UE a sítě.

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)

## Definující specifikace

- **TS 23.292** (Rel-19) — IMS Centralized Services (ICS) Architecture
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol

---

📖 **Anglický originál a plná specifikace:** [IUA na 3GPP Explorer](https://3gpp-explorer.com/glossary/iua/)
