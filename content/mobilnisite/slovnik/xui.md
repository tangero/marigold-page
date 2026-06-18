---
slug: "xui"
url: "/mobilnisite/slovnik/xui/"
type: "slovnik"
title: "XUI – XCAP Unique Identifier"
date: 2025-01-01
abbr: "XUI"
fullName: "XCAP Unique Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/xui/"
summary: "Jedinečný identifikátor používaný v protokolu XCAP k adresování konkrétních XML dokumentů nebo uzlů uložených na XCAP serveru. Umožňuje klientům spravovat data konfigurace specifické pro služby, jako"
---

XUI je XCAP Unique Identifier (jedinečný identifikátor XCAP) používaný v protokolu XCAP k adresování konkrétních XML dokumentů nebo uzlů uložených na XCAP serveru.

## Popis

[XCAP](/mobilnisite/slovnik/xcap/) Unique Identifier (XUI) je základní součástí frameworku [XML](/mobilnisite/slovnik/xml/) Configuration Access Protocol (XCAP) definovaného 3GPP. XCAP umožňuje klientovi, jako je User Equipment (UE) nebo aplikační server, číst, zapisovat a upravovat konfigurační data aplikace uložená ve formátu XML na vzdáleném serveru, známém jako XCAP server. Tato data se často týkají služeb IMS, včetně politik autorizace presence (např. pravidla presence v aplikačním použití `org.openmobilealliance.pres-rules`), seznamů zdrojů pro konferenční hovory nebo nastavení doplňkových služeb. XUI slouží jako primární klíč pro jednoznačnou identifikaci datového dokumentu uživatele nebo konkrétního prvku v tomto dokumentu na serveru.

Architektonicky je XUI vložen do [HTTP](/mobilnisite/slovnik/http/) [URI](/mobilnisite/slovnik/uri/) používaného pro XCAP operace. Typická HTTP žádost XCAP má hierarchickou strukturu obsahující komponenty jako XCAP root, Application Unique ID ([AUID](/mobilnisite/slovnik/auid/)), XUI a selektor dokumentu s volitelným selektorem uzlu. Samotný XUI je odvozen od veřejné identity uživatele, jako je [SIP](/mobilnisite/slovnik/sip/) URI nebo [TEL](/mobilnisite/slovnik/tel/) URI. Například XUI může být vytvořen tak, že se vezme SIP URI `sip:user@example.com` a použije [URL](/mobilnisite/slovnik/url/) kódování pro vytvoření řetězce jako `sip%3Auser%40example.com`. To zajišťuje, že identifikátor je jedinečný v kontextu specifického AUID a XCAP root.

Když klient provádí XCAP operaci, vytvoří cílové URI pomocí XUI, aby přesně určil XML zdroj. Server použije XUI k nalezení úložiště dokumentů uživatele, autentizaci a autorizaci žádosti (často na základě shody autentizované identity s XUI) a následnému provedení požadované manipulace s XML, jako je GET, PUT nebo DELETE. Role XUI je klíčová pro udržení izolace dat mezi uživateli a pro umožnění škálovatelných nasazení XCAP serveru pro více tenantů. Jeho standardizovaný formát zajišťuje interoperabilitu mezi XCAP klienty a servery různých výrobců, což je zásadní pro ekosystém služeb založených na IMS.

Mimo základní CRUD operace hraje XUI také roli v mechanismech odběru. Klienti se mohou přihlásit k odběru změn konkrétních XML dokumentů pomocí frameworku SIP event notification, kde žádost o odběr odkazuje na dokument prostřednictvím jeho XCAP URI obsahujícího XUI. To umožňuje synchronizaci konfiguračních dat v reálném čase. Správa XUI, včetně jejich přidělování a mapování na identity uživatelů, je typicky řešena IMS jádrem a HSS poskytovatele služeb, což zajišťuje konzistenci v celé síti.

## K čemu slouží

XCAP Unique Identifier (XUI) byl vytvořen, aby vyřešil problém správy konfiguračních dat služeb specifických pro uživatele v sítích IP Multimedia Subsystem (IMS) standardizovaným, RESTful způsobem. Před XCAP byla konfigurace služeb často řešena proprietárními protokoly nebo vložena do složitých signalizačních toků, což vedlo k problémům s interoperabilitou a omezené flexibilitě pro uživatele při samosprávě jejich nastavení. Zavedení XCAP a tím i XUI poskytlo jednotný mechanismus založený na HTTP/XML pro manipulaci s daty, což je v souladu s paradigmaty vývoje webových aplikací.

Primární motivací bylo umožnit bohaté IMS služby jako presence, zasílání zpráv a konferenční hovory, kde uživatelé potřebují definovat komplexní politiky (např. 'kdo může vidět můj stav online'). Tyto politiky jsou přirozeně reprezentovány jako XML dokumenty. XUI poskytuje jednoduché, ale účinné schéma adresování, které umožňuje jakémukoli autorizovanému klientovi jednoznačně identifikovat a upravit konkrétní dokument uživatele bez nejednoznačnosti. Tím odděluje úložiště konfigurace od servisní logiky a podporuje škálovatelnější a udržovatelnější architekturu.

Navíc XUI usnadňuje mobilitu uživatele a scénáře s více zařízeními. Protože je identifikátor založen na trvalé veřejné identitě uživatele (jako je SIP URI), může uživatel přistupovat a upravovat nastavení svých služeb z různých zařízení nebo klientů, což zajišťuje konzistentní uživatelský zážitek. Také umožňuje síťovým operátorům bezpečně delegovat správu konfigurace na poskytovatele aplikací třetích stran, protože XUI slouží jako jasná hranice jmenného prostoru. Vytvoření XUI v rámci 3GPP Rel-12 bylo součástí širšího úsilí o dozrání IMS služebních enablerů a podporu rostoucí poptávky po přizpůsobitelných komunikačních službách.

## Klíčové vlastnosti

- Jednoznačně identifikuje XML dokument uživatele v kontextu aplikačního použití XCAP
- Odvozen od veřejné identity uživatele (např. SIP URI nebo TEL URI) a je URL-kódován pro použití v HTTP URI
- Umožňuje standardní HTTP metody (GET, PUT, DELETE) pro CRUD operace nad XML konfiguračními daty
- Zásadní pro izolaci dat a multi-tenancy v nasazeních XCAP serveru
- Používá se společně s Application Unique ID (AUID) a selektorem dokumentu k vytvoření úplného URI zdroje XCAP
- Podporuje mechanismy odběru pro oznámení o změnách dokumentu v reálném čase prostřednictvím SIP

## Související pojmy

- [XCAP – XML Configuration Access Protocol](/mobilnisite/slovnik/xcap/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP-URI – SIP Uniform Resource Identifier](/mobilnisite/slovnik/sip-uri/)

## Definující specifikace

- **TS 24.483** (Rel-19) — Mission Critical Services Management Object
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 24.623** (Rel-19) — XCAP Protocol for Supplementary Services

---

📖 **Anglický originál a plná specifikace:** [XUI na 3GPP Explorer](https://3gpp-explorer.com/glossary/xui/)
