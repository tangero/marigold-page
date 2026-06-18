---
slug: "s1-mme"
url: "/mobilnisite/slovnik/s1-mme/"
type: "slovnik"
title: "S1-MME – S1 Control Plane Interface to the Mobility Management Entity"
date: 2025-01-01
abbr: "S1-MME"
fullName: "S1 Control Plane Interface to the Mobility Management Entity"
category: "Interface"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/s1-mme/"
summary: "S1-MME je logické rozhraní řídicí roviny mezi eNodeB a MME v sítích LTE. Přenáší signalizaci pro správu mobility, zřizování relací a zabezpečení, odděluje řídicí funkce od uživatelských dat za účelem"
---

S1-MME je logické rozhraní řídicí roviny mezi eNodeB a MME v sítích LTE, přenášející signalizaci pro správu mobility, zřizování relací a zabezpečení.

## Popis

Rozhraní S1-MME je konkrétní implementací řídicí roviny S1 ([S1-C](/mobilnisite/slovnik/s1-c/)), která spojuje Evolved NodeB (eNodeB) v [E-UTRAN](/mobilnisite/slovnik/e-utran/) s Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v Evolved Packet Core (EPC). Jak je definováno ve specifikacích 3GPP, jde o logické rozhraní, které fyzicky prochází IP transportní sítí a využívá na transportní vrstvě Stream Control Transmission Protocol ([SCTP](/mobilnisite/slovnik/sctp/)) pro zajištění spolehlivého, uspořádaného a kontrolovaného doručování signalizačních zpráv. Rozhraní používá S1 Application Protocol ([S1AP](/mobilnisite/slovnik/s1ap/)), který zapouzdřuje širokou škálu procedur a zpráv nezbytných pro řízení a správu připojení UE. S1-MME má povahu point-to-point, což znamená, že každé eNodeB navazuje jednu nebo více asociací S1-MME s MME, často v konfiguraci poolu pro zvýšení spolehlivosti a distribuce zátěže.

Klíčové provozní aspekty S1-MME zahrnují zpracování Initial UE Context Setup, kdy MME poskytne eNodeB parametry zabezpečení a QoS specifické pro UE po autentizaci; Bearer Management, zahrnující aktivaci, modifikaci a deaktivaci Evolved Radio Access Bearers (E-RABs) pro podporu toků uživatelských dat; a Mobility Management, který zahrnuje procedury přípravy, provedení a zrušení handoveru pro UE pohybující se mezi buňkami nebo přístupovými technologiemi. Rozhraní také podporuje Paging, kdy MME iniciuje pagingové požadavky k nalezení neaktivních UE, a [NAS](/mobilnisite/slovnik/nas/) Transport, který umožňuje transparentní přenos zpráv Non-Access Stratum (např. pro připojení nebo aktualizaci tracking area) mezi UE a MME. Dále S1-MME usnadňuje procedury Error Indication a Reset pro udržení integrity rozhraní a zotavení z poruch.

Z architektonického hlediska je S1-MME navrženo se zaměřením na škálovatelnost a flexibilitu, podporuje funkce jako S1-flex, které umožňují eNodeB připojit se k více MME v rámci pool area. To umožňuje vyrovnávání zátěže a redundanci, čímž snižuje riziko narušení služeb při výpadku MME. Rozhraní striktně odděluje signalizaci řídicí roviny od dat uživatelské roviny (která proudí přes [S1-U](/mobilnisite/slovnik/s1-u/)), v souladu s principem Control and User Plane Separation (CUPS). Toto oddělení umožňuje nezávislé škálování a optimalizaci síťových funkcí – například MME mohou být centralizována pro efektivní zpracování signalizace, zatímco eNodeB a brány uživatelské roviny jsou distribuovány pro minimalizaci latence. V praxi je S1-MME klíčové pro udržování stavů UE (např. ECM-IDLE nebo ECM-CONNECTED), vynucování bezpečnostních politik prostřednictvím správy klíčů a koordinaci alokace rádiových zdrojů, čímž tvoří páteř efektivní řídicí roviny LTE s nízkou latencí.

## K čemu slouží

Rozhraní S1-MME bylo vyvinuto v 3GPP Release 8 jako klíčový prvek architektury LTE/EPC za účelem překonání neefektivit předchozích systémů 3GPP, jako je UMTS. V UMTS zahrnovalo rozhraní řídicí roviny (Iu-CS a Iu-PS) Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) jako zprostředkovatele mezi NodeB a jádrem sítě, což přidávalo složitost, latenci a potenciální úzká místa. S1-MME bylo vytvořeno pro zploštění sítě tím, že umožnilo přímou signalizaci mezi základnovou stanicí (eNodeB) a řídicí entitou (MME), čímž odstranilo vrstvu RNC. Tento návrh snižuje signalizační zpoždění, zjednodušuje topologii sítě a zlepšuje odezvu na mobilní události a správu relací, což je klíčové pro podporu vysokorychlostních datových služeb a aplikací v reálném čase.

Historicky potřeba S1-MME vyplynula z nutnosti přechodu na plně IP síťovou architekturu, která by zvládla exponenciální růst mobilního datového provozu, podnícený rozšířením chytrých telefonů a aplikací náročných na šířku pásma. Oddělením řídicí roviny (přes S1-MME) od uživatelské roviny umožnilo 3GPP operátorům nasazovat a škálovat síťové funkce nezávisle – například koncentrovat MME pro nákladově efektivní zpracování signalizace, zatímco eNodeB jsou distribuována pro pokrytí. Toto oddělení také usnadnilo zavedení pokročilých funkcí, jako je sdílení sítě, kde více operátorů může používat sdílenou infrastrukturu rádiového přístupu při zachování nezávislého řízení jádra, a položilo základy pro budoucí vývoj směrem k 5G tím, že poskytlo flexibilní rozhraní, které lze rozšířit o nové procedury.

Navíc S1-MME řeší kritické otázky spolehlivosti a škálovatelnosti prostřednictvím mechanismů jako MME pooling a S1-flex, které distribuují řídicí provoz přes více uzlů MME, aby se předešlo jediným bodům selhání a dynamicky vyvažovala zátěž. To byl významný pokrok oproti dřívějším architekturám, kde selhání řídicího uzlu mohlo vést k rozsáhlým výpadkům. Standardizací S1-MME napříč releasy zajistilo 3GPP zpětnou kompatibilitu a hladkou spolupráci se staršími systémy, což umožnilo postupné upgrady sítě. Konečným účelem S1-MME je poskytnout robustní, efektivní a škálovatelné rozhraní řídicí roviny, které podporuje klíčové funkce LTE, jako je správa mobility, bezpečnostní autentizace a řízení bearerů, čímž zlepšuje celkový výkon sítě a uživatelský zážitek.

## Klíčové vlastnosti

- Implementuje SCTP pro spolehlivý transport signalizace s podporou multi-homingu
- Využívá protokol S1AP pro komplexní signalizační procedury mezi eNodeB a MME
- Umožňuje zřízení počátečního kontextu UE s parametry zabezpečení a QoS
- Podporuje správu E-RAB pro dynamické řízení bearerů
- Usnadňuje procedury handoveru včetně intra-LTE a inter-RAT
- Poskytuje transport NAS pro end-to-end komunikaci mezi UE a MME

## Související pojmy

- [S1-C – S1 Control Plane](/mobilnisite/slovnik/s1-c/)
- [S1-U – S1 User Plane Interface](/mobilnisite/slovnik/s1-u/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [S1AP – S1 Application Protocol](/mobilnisite/slovnik/s1ap/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.410** (Rel-19) — S1 Interface: General Aspects and Principles

---

📖 **Anglický originál a plná specifikace:** [S1-MME na 3GPP Explorer](https://3gpp-explorer.com/glossary/s1-mme/)
