---
slug: "cer"
url: "/mobilnisite/slovnik/cer/"
type: "slovnik"
title: "CER – Capabilities Exchange Request"
date: 2025-01-01
abbr: "CER"
fullName: "Capabilities Exchange Request"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cer/"
summary: "Zpráva protokolu Diameter používaná k zahájení výměny informací o schopnostech mezi uzly Diameter. Umožňuje uzlům zjistit vzájemně podporované aplikace, funkce specifické pro výrobce a bezpečnostní me"
---

CER je zpráva protokolu Diameter používaná k zahájení výměny informací o podporovaných schopnostech mezi uzly (peers) za účelem zjištění podporovaných aplikací a funkcí pro vzájemnou spolupráci v sítích 3GPP.

## Popis

Capabilities Exchange Request (CER) je základní příkaz v základním protokolu Diameter (RFC 6733), který je rozsáhle používán v architekturách 3GPP pro autentizaci, autorizaci a účtování ([AAA](/mobilnisite/slovnik/aaa/)). Jako protokol typu peer-to-peer vyžaduje Diameter, aby si uzly před zahájením komunikace specifické pro danou aplikaci stanovily vzájemné schopnosti. Zpráva CER je úvodní požadavek odeslaný během fáze výměny schopností, která probíhá poté, co je mezi dvěma uzly Diameter (např. mezi Diameter klientem, jako je Policy and Charging Rules Function - PCRF, a Diameter serverem, jako je Home Subscriber Server - [HSS](/mobilnisite/slovnik/hss/)) navázáno transportní spojení (např. TCP nebo SCTP). CER obsahuje sadu atribut-hodnota párů ([AVP](/mobilnisite/slovnik/avp/)), které inzerují identitu odesílatele, podporované Diameter aplikace, bezpečnostní mechanismy a schopnosti specifické pro výrobce.

Po přijetí CER musí uzel Diameter odpovědět zprávou Capabilities Exchange Answer (CEA). Proces výměny zahrnuje vzájemné porovnání inzerovaných schopností oběma uzly. Mezi klíčové AVP v rámci CER patří Origin-Host a Origin-Realm, které identifikují odesílatele, Host-IP-Address, který uvádí IP adresy uzlu, Vendor-Id, udávající výrobce implementace Diameter, Product-Name a především AVP Supported-Vendor-Id a Auth-Application-Id. AVP Auth-Application-Id uvádí konkrétní Diameter aplikace, které uzel podporuje, například 3GPP-specifické aplikace pro rozhraní S6a/S6d (HSS-MME), Gx (PCRF-PCEF) nebo Rx (AF-PCRF). To umožňuje uzlům zjistit, zda sdílejí společnou podporu aplikací nezbytnou pro následné servisní požadavky.

Úspěšná výměna vytvoří spojení mezi uzly Diameter, které je připraveno pro komunikaci na aplikační úrovni. Pokud jsou schopnosti nekompatibilní – například pokud není podporována žádná společná Diameter aplikace – mohou se uzly odpojit. Výměna CER/CEA také vyjednává bezpečnostní mechanismy, ačkoli v mnoha nasazeních 3GPP je bezpečnost na transportní vrstvě (např. [IPsec](/mobilnisite/slovnik/ipsec/) nebo TLS) povinná. Toto navázání spojení je klíčové pro spolehlivost sítě, neboť předchází chybným konfiguracím a zajišťuje, že komunikují pouze autorizované a kompatibilní uzly. Tvoří tak základ pro bezpečné a efektivní AAA operace napříč jádrem sítě, včetně řízení politik, správy mobility a autentizace účastníků.

## K čemu slouží

CER existuje, aby řešil základní problém interoperability a správy relací v distribuovaných sítích založených na Diameter od více výrobců. Před Diameter byl pro [AAA](/mobilnisite/slovnik/aaa/) používán protokol RADIUS, který měl omezení v škálovatelnosti, podpoře převzetí služeb při selhání a v prostoru atributů. Diameter byl navržen jako jeho nástupce a mechanismus výměny schopností, zahájený CER, byl zaveden, aby umožnil dynamické zjišťování a vyjednávání mezi uzly. To je nezbytné, protože sítě 3GPP se skládají z mnoha síťových funkcí od různých výrobců, které musí bezproblémově spolupracovat. Bez standardizované výměny schopností by se uzly musely spoléhat na statickou konfiguraci, která je náchylná k chybám, nepružná a obtížně spravovatelná ve velkých a vyvíjejících se sítích.

CER umožňuje automatické zjišťování uzlů a inzerování schopností, což je zásadní pro nasazení sítí typu plug-and-play a robustní scénáře převzetí služeb při selhání. V případě výpadku uzlu může záložní uzel navázat nové spojení a okamžitě prostřednictvím CER inzerovat své schopnosti, což umožní rychlé obnovení služeb. Navíc, jak 3GPP v jednotlivých vydáních zavádělo nové služby a rozhraní (např. řízení politik ve vydání 7, VoLTE ve vydání 8), mechanismus CER umožnil uzlům dynamicky deklarovat podporu nových Diameter aplikací. Tím byla architektura připravena na budoucnost a umožnila hladké zavádění nových funkcionalit bez nutnosti rozsáhlého překonfigurování stávajících síťových prvků, čímž se snížily provozní náklady a minimalizovaly výpadky služeb.

## Klíčové vlastnosti

- Zahajuje navázání spojení a vyjednávání schopností mezi uzly Diameter
- Inzeruje podporované Diameter aplikace prostřednictvím AVP Auth-Application-Id
- Komunikuje schopnosti specifické pro výrobce prostřednictvím AVP Vendor-Id a Supported-Vendor-Id
- Vyměňuje si informace o identifikaci a adresování uzlů (Origin-Host, Host-IP-Address)
- Vyjednává bezpečnostní a účtovací schopnosti na úrovni protokolu
- Umožňuje dynamické zjišťování uzlů a interoperabilitu v sítích s více výrobci

## Definující specifikace

- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TS 26.226** (Rel-19) — Cellular Text Telephone Modem (CTM)
- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP

---

📖 **Anglický originál a plná specifikace:** [CER na 3GPP Explorer](https://3gpp-explorer.com/glossary/cer/)
