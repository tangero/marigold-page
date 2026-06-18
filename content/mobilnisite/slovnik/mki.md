---
slug: "mki"
url: "/mobilnisite/slovnik/mki/"
type: "slovnik"
title: "MKI – Master Key Identifier"
date: 2026-01-01
abbr: "MKI"
fullName: "Master Key Identifier"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mki/"
summary: "Identifikátor hlavního klíče (Master Key) používaný v bezpečnostních protokolech 3GPP, který umožňuje síti a uživatelskému zařízení (UE) vybrat správný kryptografický klíč ze sady uložených klíčů pro"
---

MKI je identifikátor hlavního klíče (Master Key), který umožňuje síti a uživatelskému zařízení (UE) vybrat správný kryptografický klíč z uložené sady pro zabezpečení komunikačních relací.

## Popis

Master Key Identifier (MKI) je pole používané v bezpečnostních architekturách 3GPP k identifikaci konkrétního hlavního klíče (Master Key, MK) v rámci hierarchie klíčů. Hlavní klíč je dlouhodobý kryptografický klíč, ze kterého jsou odvozovány relací specifické klíče pro ochranu provozu v uživatelské a řídicí rovině. MKI umožňuje jak uživatelskému zařízení (UE), tak síti (např. bezpečnostním funkcím jádra sítě) jednoznačně odkazovat a vybrat příslušný hlavní klíč, když je uloženo více klíčů, což je zásadní pro efektivní správu klíčů, obnovu relací a scénáře předávání spojení.

V praxi je MKI zahrnuto v bezpečnostně chráněných protokolových zprávách, například v procedurách zabezpečení na vrstvě [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum) nebo [AS](/mobilnisite/slovnik/as/) (Access Stratum). Během procesu autentizace a dohody klíčů ([AKA](/mobilnisite/slovnik/aka/)) v systémech EPS nebo 5G je například navázán hlavní klíč (K_[ASME](/mobilnisite/slovnik/asme/) v EPS, K_[AUSF](/mobilnisite/slovnik/ausf/) v 5G [SA](/mobilnisite/slovnik/sa/)). Zatímco samotný klíč není přenášen, jeho identifikátor může být použit v následné signalizaci. MKI pomáhá korelovat odvozené relací klíče (jako K_[eNB](/mobilnisite/slovnik/enb/), K_NG-RAN nebo šifrovací/integritní klíče) zpět k jejich kořenovému hlavnímu klíči. To je obzvláště důležité, když má uživatelské zařízení více současných bezpečnostních kontextů (např. pro více síťových řezů, připojení [PDN](/mobilnisite/slovnik/pdn/) nebo během předávání spojení mezi různými rádiovými technologiemi) a potřebuje označit, který kontext a podkladový hlavní klíč má být použit.

MKI je definováno a používáno v různých specifikacích 3GPP pokrývajících různé rozhraní a protokoly. V kontextu IMS a multimediálních služeb (specifikováno v TS 24.380, TS 24.581) je MKI používáno v rámci protokolu Secure Real-time Transport Protocol (SRTP) a jeho klíčového správního protokolu MIKEY (Multimedia Internet Keying) k identifikaci kryptografických relací klíčů používaných pro šifrování mediálních proudů. Zde MKI umožňuje přijímači identifikovat, který klíč z jeho úložiště klíčů má být použit k dešifrování příchozího SRTP paketu, když byl klíčový materiál aktualizován nebo je používáno více klíčů.

Architektonicky je MKI spíše štítek nebo index než klíč sám o sobě. Jeho délka a formát mohou být specifikovány aplikací nebo protokolem, který jej používá. Síťové entity zodpovědné za správu zabezpečení, jako je Authentication Server Function (AUSF), Security Anchor Function (SEAF) nebo aplikační servery v IMS, zajišťují, že hodnoty MKI jsou koordinovány a srozumitelné oběma koncovým bodům. Použití MKI zvyšuje flexibilitu a robustnost bezpečnostních protokolů tím, že umožňuje rotaci klíčů bez přerušení služby, podporu scénářů s předem sdílenými klíči a efektivní správu více bezpečnostních asociací.

## K čemu slouží

MKI bylo zavedeno k řešení problému identifikace a výběru klíčů ve scénářích, kde je k dispozici více kryptografických klíčů nebo je třeba je v čase spravovat. V raných mobilních komunikačních systémech byla správa klíčů jednodušší, často zahrnovala pouze jeden aktivní pár klíčů na účastníka. S rostoucí složitostí služeb, zavedením IP Multimedia Subsystem (IMS) a požadavky na dopředné utajení a periodické aktualizace klíčů však byly zapotřebí mechanismy, které by jednoznačně identifikovaly, který klíč má být pro danou relaci nebo paket použit.

Bez identifikátoru jako je MKI by měly koncové body potíže se správou více klíčů, zejména během přechodů, jako je předávání spojení mezi buňkami nebo změny bezpečnostního kontextu. To by mohlo vést k selhání synchronizace, chybám při dešifrování nebo přerušení služby. MKI poskytuje odlehčenou signalizační metodu v pásmu pro odkazování na správný hlavní nebo relací klíč, což umožňuje plynulejší správu životního cyklu klíčů včetně jejich odvozování, aktualizace a odvolání.

Jeho vytvoření bylo motivováno potřebou škálovatelného zabezpečení pro multimediální služby přes IP (např. VoLTE, ViLTE) a později pro vylepšené zabezpečení jádra sítě v EPS a 5G. Standardizací pole MKI napříč různými protokoly (NAS, AS, SRTP/MIKEY) zajistilo 3GPP interoperabilitu mezi síťovými zařízeními a uživatelskými zařízeními od různých výrobců. Řeší omezení implicitního nebo stavového výběru klíčů a poskytuje explicitní robustní mechanismus, který je klíčový pro udržení bezpečné a nepřetržité komunikace v moderních mobilních sítích s jejich množstvím souběžných relací a pokročilých služeb.

## Klíčové vlastnosti

- Jednoznačně identifikuje hlavní klíč nebo bezpečnostní kontext ze sady uložených klíčů
- Umožňuje správný výběr klíče během navazování relace, předávání spojení a obnovy relace
- Používá se na více protokolových vrstvách včetně zabezpečení NAS, AS a IMS/SRTP
- Podporuje správu životního cyklu klíčů včetně jejich aktualizace a rotace bez přerušení služby
- Usnadňuje správu více současných bezpečnostních kontextů (např. pro síťové řezy)
- Napomáhá synchronizaci kryptografického stavu mezi uživatelským zařízením a síťovými entitami

## Související pojmy

- [MIKEY – Multimedia Internet KEYing](/mobilnisite/slovnik/mikey/)
- [SRTP – Secure Real-time Transport Protocol](/mobilnisite/slovnik/srtp/)

## Definující specifikace

- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.581** (Rel-19) — MCVideo Media Plane Control Protocol Specification
- **TS 33.179** (Rel-13) — MCPTT Security Architecture and Procedures
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.246** (Rel-19) — MBMS Security Specification
- **TS 33.879** (Rel-13) — MCPTT Security Study

---

📖 **Anglický originál a plná specifikace:** [MKI na 3GPP Explorer](https://3gpp-explorer.com/glossary/mki/)
