---
slug: "du"
url: "/mobilnisite/slovnik/du/"
type: "slovnik"
title: "DU – Triple DES Unwrap Plug-in"
date: 2026-01-01
abbr: "DU"
fullName: "Triple DES Unwrap Plug-in"
category: "Security"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/du/"
summary: "Kryptografický zásuvný modul používaný v bezpečnostních architekturách 3GPP k rozbalení (dešifrování) klíčů, které byly zašifrovány pomocí algoritmu Triple DES (3DES). Je součástí systémů správy a dis"
---

DU je kryptografický zásuvný modul (plug-in) v rámci bezpečnostních architektur 3GPP, který rozbalí (dešifruje) klíče zašifrované pomocí Triple DES, a slouží jako kritická komponenta pro bezpečnou správu a distribuci klíčů.

## Popis

Zásuvný modul pro rozbalení Triple [DES](/mobilnisite/slovnik/des/) (DU) je softwarový nebo hardwarový kryptografický modul specifikovaný v různých technických specifikacích 3GPP. Jeho primární funkcí je provádět operaci rozbalení, což je dešifrování zabaleného (zašifrovaného) klíče. Proces zabalení typicky používá algoritmus Triple DES v konkrétním režimu, jako je algoritmus Key Wrap definovaný v RFC 3394, k ochraně citlivého klíče (např. relakového nebo kořenového klíče) během přenosu přes potenciálně nezabezpečené kanály. Modul DU obsahuje potřebnou logiku a kryptografické primitivy pro přijetí zabaleného klíče, aplikaci správných kroků dešifrování 3DES pomocí předem sdíleného nebo odvozeného šifrovacího klíče klíče ([KEK](/mobilnisite/slovnik/kek/)) a výstup čistého textu klíčového materiálu pro použití přijímající entitou.

Z architektonického hlediska DU není samostatný síťový uzel, ale funkční komponenta integrovaná do větších bezpečnostních entit. Může být například součástí Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), Authentication Centre (AuC) nebo síťového prvku provádějícího správu klíčů v architektuře Generic Bootstrapping Architecture ([GBA](/mobilnisite/slovnik/gba/)). Jeho činnost je spuštěna, když entita přijme klíč zabalený pro jeho ochranu. Modul použije příslušný KEK, který je bezpečně znám jak zabalující, tak rozbalující straně, k dešifrování šifrového textu. Specifikace podrobně popisuje přesné kryptografické parametry, včetně použití blokové šifry 3DES s 168bitovým klíčem (skládajícím se ze tří 56bitových DES klíčů) a konkrétních schémat pro odsazení nebo formátování vyžadovaných pro interoperabilitu.

Role DU v síti je zásadní pro bezpečné protokoly pro navázání a distribuci klíčů. Poskytnutím standardizované metody pro rozbalení klíčů zajišťuje, že zařízení různých výrobců si mohou bezpečně vyměňovat kryptografický materiál. To je nezbytné pro funkce jako autentizace, šifrování a ochrana integrity na rozhraní rádiového přístupu a uvnitř jádra sítě. Činnost modulu je často transparentní pro protokoly vyšších vrstev, které jednoduše vyžadují službu rozbalení klíče. Jeho správná implementace je ověřována prostřednictvím testů shody specifikovaných v dokumentech jako 31.113, což zajišťuje robustní zabezpečení v celém ekosystému.

## K čemu slouží

DU byl vytvořen k řešení potřeby standardizované, bezpečné metody přenosu kryptografických klíčů mezi síťovými funkcemi v systémech 3GPP. V raných vydáních, jako je Rel-8, kdy se sítě vyvíjely k podpoře sofistikovanějších služeb jako IMS a mobilní širokopásmový přístup, se bezpečná distribuce relakových klíčů z autentizačních serverů do obslužných uzlů stala prvořadou. Předchozí ad-hoc nebo výrobci specifické metody přenosu klíčů představovaly rizika interoperability a potenciální bezpečnostní zranitelnosti. Modul DU, založený na zavedeném algoritmu Triple [DES](/mobilnisite/slovnik/des/), poskytl dobře definovanou kryptografickou operaci, kterou bylo možné spolehlivě implementovat napříč odvětvím.

Motivací pro specifikaci takového modulu bylo oddělení složitých kryptografických operací od základní logiky síťových entit. Definováním přesné funkce rozbalení 3GPP zajistilo, že bezpečnostně kritický úkol dešifrování klíče bude prováděn správně a konzistentně bez ohledu na výrobce implementujícího [HSS](/mobilnisite/slovnik/hss/) nebo jiný bezpečnostní modul. Tento přístup také usnadnil vývoj kryptografických algoritmů; zatímco DU konkrétně zpracovává 3DES, model zásuvného modulu umožňuje definici dalších modulů pro rozbalení pro novější algoritmy (jako je [AES](/mobilnisite/slovnik/aes/)) v pozdějších vydáních, což podporuje postupnou migraci. DU vyřešil problém, jak bezpečně doručit klíče, které chrání uživatelský provoz a signalizaci, což je základním požadavkem pro služby důvěrnosti a integrity jakékoli mobilní sítě.

## Klíčové vlastnosti

- Implementuje dešifrovací algoritmus Triple DES (3DES) pro rozbalení klíčů
- Podporuje standardizované formáty zabalení klíčů dle specifikací 3GPP a IETF RFC
- Integrován jako funkční komponenta do větších bezpečnostních entit, jako je HSS/AuC
- Umožňuje bezpečnou interoperabilitu pro distribuci klíčů mezi zařízeními více výrobců
- Podléhá testům shody pro zajištění správné kryptografické operace
- Pracuje se šifrovacím klíčem klíče (KEK) navázaným bezpečnými prostředky

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [AUC – Authentication Centre](/mobilnisite/slovnik/auc/)

## Definující specifikace

- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TS 25.415** (Rel-19) — Iu Interface User Plane Protocol
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 38.201** (Rel-19) — NR Physical Layer General Description
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TR 38.838** (Rel-17) — Study on XR Evaluations for NR

---

📖 **Anglický originál a plná specifikace:** [DU na 3GPP Explorer](https://3gpp-explorer.com/glossary/du/)
