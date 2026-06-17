---
slug: "hss"
url: "/mobilnisite/slovnik/hss/"
type: "slovnik"
title: "HSS – Home Subscriber Server"
date: 2026-01-01
abbr: "HSS"
fullName: "Home Subscriber Server"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hss/"
summary: "HSS je centrální hlavní databáze pro informace o uživateli a předplatném v sítích 3GPP. Ukládá uživatelské profily, provádí autentizaci a autorizaci a spravuje poskytování služeb a mobilitu. Jedná se"
---

HSS je centrální hlavní databáze v sítích 3GPP, která ukládá uživatelské profily, provádí autentizaci a autorizaci a spravuje poskytování služeb a mobilitu.

## Popis

Home Subscriber Server (HSS) je primární úložiště dat o účastnících a autentizační centrum v paketově orientovaných jádrových sítích 3GPP, včetně IP Multimedia Subsystem (IMS). Z architektonického hlediska představuje vývoj a sloučení Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) a Authentication Center (AuC) ze sítí GSM, rozšířené pro IP služby. Nachází se v rámci Home Public Land Mobile Network ([HPLMN](/mobilnisite/slovnik/hplmn/)) a komunikuje s mnoha entitami jádrové sítě prostřednictvím rozhraní Cx, Sh a S6a/S6d založených na protokolu Diameter. Jeho ústřední rolí je správa identity uživatele, servisního profilu a informací o poloze, což jej činí nepostradatelným pro navazování relací, správu mobility a autorizaci služeb.

HSS ukládá pro každého účastníka komplexní soubor trvalých dat, známý jako Uživatelský profil. To zahrnuje International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)), Mobile Subscriber Integrated Services Digital Network Number ([MSISDN](/mobilnisite/slovnik/msisdn/)), parametry Quality of Service (QoS) k předplatnému a access point names ([APN](/mobilnisite/slovnik/apn/)) pro datovou konektivitu. Pro služby IMS také ukládá uživatelovu Private User Identity ([IMPI](/mobilnisite/slovnik/impi/)), Public User Identity ([IMPU](/mobilnisite/slovnik/impu/)) a přidružené servisní profily, které definují možnosti telefonních a multimediálních služeb. Při připojování k síti a navazování relace HSS spolupracuje s dalšími uzly: poskytuje autentizační vektory (RAND, XRES, [AUTN](/mobilnisite/slovnik/autn/), CK, IK) Mobility Management Entity (MME) nebo Serving-Call Session Control Function (S-CSCF) k ověření identity uživatele a generování šifrovacích a integritních klíčů pro zabezpečenou komunikaci.

Kromě autentizace je HSS klíčový pro správu mobility. Sleduje aktuální obslužný uzel uživatele (např. MME v LTE, AMF v 5G) a na žádost tyto informace poskytuje entitám, jako je Gateway Mobile Switching Center (GMSC), pro směrování příchozích hovorů. Také podporuje poskytování služeb tím, že notifikuje aplikační servery (prostřednictvím rozhraní Sh) o změnách v uživatelském profilu nebo registračním stavu. V sítích 5G jsou jeho funkce částečně převzaty Unified Data Management (UDM), ale HSS zůstává klíčový pro legacy scénáře a scénáře pro vzájemné propojení sítí. Jeho robustnost a vysoká dostupnost jsou prvořadé, protože představuje jediný bod selhání pro správu účastníků; proto je často nasazován v redundantních, geograficky oddělených konfiguracích.

## K čemu slouží

HSS byl vytvořen, aby řešil omezení HLR/AuC z éry GSM v kontextu plně IP sítí a zavedení IP Multimedia Subsystem (IMS). Tradiční HLR byl navržen primárně pro přepojování okruhů hlasu a SMS s využitím protokolu MAP. Jak se sítě 3GPP vyvíjely, aby podporovaly vysokorychlostní paketová data a bohaté multimediální služby (VoIP, videohovory, presence), byla vyžadována flexibilnější, IP-centrická a na služby orientovaná databáze účastníků. HSS byl standardizován v 3GPP Release 5 jako součást architektury IMS, aby tuto potřebu naplnil, a poskytuje tak jednotné úložiště dat schopné podporovat jak legacy mobilitu v přepojování okruhů, tak nové IMS služby v přepojování paketů.

Jeho vytvoření vyřešilo několik klíčových problémů. Za prvé konsolidovalo data o účastnících, čímž odstranilo potřebu samostatných, synchronizovaných databází pro domény přepojování okruhů, přepojování paketů a IMS, což snížilo složitost a provozní náklady. Za druhé zavedlo protokol Diameter (který pro mnoho rozhraní nahradil SS7 MAP), jenž je vhodnější pro IP sítě, nabízí lepší zabezpečení, škálovatelnost a podporu atribut-hodnota párů (AVP) pro flexibilní výměnu dat. Za třetí umožnil sofistikované servisní profily a triggery pro IMS, což operátorům dovolilo nabízet personalizované multimediální služby. HSS se stal základním kamenem pro umožnění konvergence pevných a mobilních sítí, roamingových dohod pro datové a IMS služby a zabezpečeného přístupu k síťovým zdrojům, čímž položil základy moderního mobilního broadbandového zážitku.

## Klíčové vlastnosti

- Centralizované úložiště všech trvalých dat o účastnících a servisních profilů
- Generuje autentizační vektory a klíče pro vzájemnou autentizaci uživatele a sítě (AKA)
- Spravuje registraci uživatele a mobilitu, sleduje obslužný síťový uzel (MME, SGSN, S-CSCF)
- Podporuje rozhraní Cx, Sh, S6a, S6d a Gr založená na protokolu Diameter pro komunikaci s prvky jádrové sítě
- Umožňuje autorizaci služeb a stažení profilu pro IMS a paketové datové služby
- Umožňuje zákonné odposlechy a správu dat o účastnících pro potřeby správy operátora

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.198** (Rel-9) — Open Service Access (OSA); Stage 2
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.251** (Rel-19) — Network Sharing Stage 2 Specification
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- … a dalších 63 specifikací

---

📖 **Anglický originál a plná specifikace:** [HSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/hss/)
