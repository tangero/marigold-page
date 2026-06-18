---
slug: "gruu"
url: "/mobilnisite/slovnik/gruu/"
type: "slovnik"
title: "GRUU – Globally Routable User agent URI"
date: 2026-01-01
abbr: "GRUU"
fullName: "Globally Routable User agent URI"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gruu/"
summary: "Globálně směrovatelný URI, který jednoznačně identifikuje konkrétní instanci uživatelského agenta (UA), jako je SIP telefon nebo softwarový klient. Umožňuje přímou, bezpečnou a efektivní komunikaci ty"
---

GRUU je globálně směrovatelný URI, který jednoznačně identifikuje konkrétní instanci uživatelského agenta (User Agent) a umožňuje přímou komunikaci pro služby IMS, jako je VoLTE, díky obejití složitého proxy směrování.

## Popis

Globálně směrovatelný [URI](/mobilnisite/slovnik/uri/) uživatelského agenta (GRUU) je URI protokolu [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol), který poskytuje globálně jednoznačnou a směrovatelnou adresu pro konkrétní instanci uživatelského agenta ([UA](/mobilnisite/slovnik/ua/)) v síti IMS (IP Multimedia Subsystem). Na rozdíl od veřejné uživatelské identity (např. SIP URI ve tvaru sip:user@domain.com), která je asociována s uživatelem a může být registrována z více zařízení, je GRUU vázán na jedinou instanci UA a její aktuální registraci. Toto vázání je klíčové pro umožnění přímé komunikace s konkrétním zařízením, zejména ve scénářích, kde je jedna veřejná uživatelská identita sdílena mezi více koncovými body, jako je smartphone, tablet a softphone v počítači. GRUU je vytvořen a přidělen sítí IMS, konkrétně funkcí [S-CSCF](/mobilnisite/slovnik/s-cscf/) (Serving-Call Session Control Function), během procesu registrace. Obsahuje prvky, které zajišťují globální směrovatelnost zpět do domovské sítě uživatele a ke konkrétní instanci S-CSCF, která registraci obsluhuje. To umožňuje externím entitám směrovat požadavky SIP (jako INVITE pro hovor) přímo ke správnému UA bez nutnosti složitých procedur vyhledávání.

Mechanismus GRUU funguje ve dvou základních formách: veřejné (public) a dočasné (temporary). Veřejné GRUU je dlouhodobě platný a stabilní URI, které může být publikováno v adresářích nebo použito pro trvalý kontakt. Je odvozeno od veřejné služební identity uživatele a obsahuje jednoznačný identifikátor instance (často [UUID](/mobilnisite/slovnik/uuid/)) pro konkrétní UA. Dočasné GRUU je vygenerováno pro jednu instanci registrace a zneplatní se při odregistrování UA; používá se pro komunikaci citlivou na soukromí, kde není žádoucí odhalit stabilní identifikátor. Když se UA registruje v síti IMS, zahrne podporu pro GRUU ve svém REGISTER požadavku prostřednictvím SIP option tagu 'gruu' a může poskytnout svůj identifikátor instance. S-CSCF po úspěšné autentizaci a registraci GRUU vygeneruje a vrátí je UA v odpovědi 200 OK na REGISTER požadavek, v rámci hlavičky 'P-Asserted-Identity' nebo vyhrazené hlavičky 'GRUU'. UA poté tyto GRUU používá jako hodnotu pole Contact header v následných požadavcích iniciujících SIP dialog.

Z pohledu síťové architektury je GRUU základním kamenem pro umožnění pokročilých služeb IMS. Umožňuje S-CSCF udržovat přesné mapování mezi veřejnou uživatelskou identitou, GRUU a IP adresou/portem registrovaného UA. Toto přímé mapování je nezbytné pro funkce jako call forking (kdy hovor na jednu veřejnou identitu vyzvoní na více zařízeních), kontinuita relace a zasílání zpráv. Když příchozí SIP požadavek cílí na GRUU, může jej funkce [I-CSCF](/mobilnisite/slovnik/i-cscf/) (Interrogating-CSCF) nebo externí síť směrovat na základě doménové části GRUU do domovské sítě uživatele. S-CSCF v domovské síti pak může pomocí GRUU přeposlat požadavek přímo ke správnému UA bez nutnosti provádět nové vyhledání registrace. Tím odpadá potřeba, aby [B2BUA](/mobilnisite/slovnik/b2bua/) (back-to-back user agent) spravoval směrování specifické pro zařízení, což zjednodušuje signalizační cestu a snižuje latenci. GRUU tedy poskytuje standardizované a škálovatelné řešení pro adresování zařízení v rámci vysoce distribuovaného a vícerozchodového prostředí moderních nasazení IMS.

## K čemu slouží

GRUU bylo zavedeno, aby vyřešilo základní problém adresování v architekturách [SIP](/mobilnisite/slovnik/sip/) a raného IMS: jak dosáhnout konkrétního zařízení z mnoha asociovaných se stejnou uživatelskou identitou. Před zavedením GRUU používalo SIP kontaktní adresy (kombinace IP:port), které nejsou globálně směrovatelné, zejména za NAT (Network Address Translation) nebo firewally, a nejsou stabilní napříč relacemi. To činilo přímou komunikaci mezi zařízeními, klíčovou pro služby jako instant messaging, přenos souborů a určité optimalizace komunikace v reálném čase, nespolehlivou a složitou. Absence stabilního, směrovatelného identifikátoru pro instanci UA také bránila funkcím, jako je řízení call forkingu a poskytování služeb specifických pro zařízení.

Motivace pro GRUU vycházela z vývoje IMS jako platformy pro doručování služeb multimediální komunikace přesahující základní hlas. Jak uživatelé začali vlastnit více zařízení (smartphony, tablety, notebooky) všechna registrovaná pod stejnou SIP identitou, potřebovala síť způsob, jak je pro účely směrování a servisní logiky rozlišit. Například pro odeslání zprávy pouze na uživatelův tablet nebo pro zajištění, že videohovor bude navázán na zařízení s nejlepšími schopnostmi. GRUU poskytuje tuto přesnou identifikaci koncového bodu. Jeho vytvoření bylo hnáno požadavky v 3GPP Release 7 pro IMS Multimedia Telephony a později pro Rich Communication Services (RCS), které vyžadovaly efektivní, bezpečné a přímé komunikační cesty mezi uživatelskými agenty pro podporu pokročilých funkcí, jako je zasílání zpráv v režimu relace, přenos souborů a sdílení geolokace.

GRUU dále řeší obavy o soukromí a bezpečnost. Varianta dočasného GRUU umožňuje uživateli zapojit se do komunikační relace bez odhalení své trvalé veřejné identity nebo stabilního identifikátoru zařízení druhé straně. To je klíčové pro prevenci sledování a nežádané komunikace. Poskytnutím jak veřejné, tak dočasné formy GRUU vyvažuje potřebu trvalého adresování (pro služby jako zpětné volání do hlasové schránky) a soukromí. Stalo se tak nezbytným prvkem umožňujícím důvěryhodný a funkční ekosystém vícerozchodové multimediální komunikace v rámci standardizovaného 3GPP IMS rámce.

## Klíčové vlastnosti

- Globálně směrovatelný SIP URI pro konkrétní instanci uživatelského agenta
- Podporuje jak veřejnou (stabilní), tak dočasnou (se zvýšeným soukromím) formu
- Přiděluje jej S-CSCF během registrace v IMS
- Umožňuje přímé end-to-end signalizace SIP mezi UA
- Nezbytné pro funkce IMS jako call forking, zasílání zpráv a kontinuita relace
- Obsahuje jednoznačný identifikátor instance pro rozlišení mezi více zařízeními stejného uživatele

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)
- [SIP-URI – SIP Uniform Resource Identifier](/mobilnisite/slovnik/sip-uri/)

## Definující specifikace

- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TR 23.794** (Rel-17) — Study on enhanced IMS to 5GC integration
- **TS 23.820** (Rel-9) — IMS Restoration Procedures
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 24.429** (Rel-7) — Explicit Communication Transfer (ECT) Service Specification
- **TS 24.529** (Rel-8) — Explicit Communication Transfer (ECT) Simulation Service
- **TS 24.615** (Rel-19) — Communication Waiting (CW) Service Protocol
- **TS 24.629** (Rel-19) — Explicit Communication Transfer (ECT) Protocol
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 29.292** (Rel-19) — IMS Centralized Services (ICS) Interworking
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [GRUU na 3GPP Explorer](https://3gpp-explorer.com/glossary/gruu/)
