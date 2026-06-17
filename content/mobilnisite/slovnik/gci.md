---
slug: "gci"
url: "/mobilnisite/slovnik/gci/"
type: "slovnik"
title: "GCI – Global Cable Identifier"
date: 2025-01-01
abbr: "GCI"
fullName: "Global Cable Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gci/"
summary: "Globální identifikátor kabelové sítě (GCI) je jedinečný identifikátor používaný ve specifikacích 3GPP k jednoznačné identifikaci přístupového bodu kabelové sítě nebo kabelového modemu. Hraje roli v ko"
---

GCI je jedinečný identifikátor používaný ve specifikacích 3GPP k jednoznačné identifikaci přístupového bodu kabelové sítě nebo kabelového modemu pro konvergenci pevných a mobilních sítí.

## Popis

Globální identifikátor kabelové sítě (GCI) je standardizovaný identifikátor definovaný ve specifikacích 3GPP k jednoznačné identifikaci kabelového modemu nebo koncového bodu kabelové sítě v rámci kabelové širokopásmové infrastruktury. Používá se ve scénářích zahrnujících konvergenci pevných a mobilních sítí, zejména když mobilní páteřní síť potřebuje autentizovat a spravovat uživatelské zařízení (UE), které přistupuje ke službám přes důvěryhodnou ne-3GPP přístupovou síť, jako je kabelová síť založená na standardu [DOCSIS](/mobilnisite/slovnik/docsis/) nebo jiných standardech. GCI je strukturován tak, aby poskytoval globální jedinečnost, a je typicky používán v rámci autentizačních a autorizačních protokolů. Například v kontextu architektury Evolved Packet Core (EPC) a 5G Core (5GC), když se UE připojuje přes důvěryhodný ne-3GPP přístup, může síť použít identifikátory jako GCI (spolu s dalšími) k určení konkrétního přístupového bodu a aplikování příslušných politik. GCI může být přenášen v rámci autentizačních výměn, například v metodách Extensible Authentication Protocol ([EAP](/mobilnisite/slovnik/eap/)), nebo v rozhraních pro řízení politik. Specifikace jako 3GPP TS 23.003 (Číslování, adresování a identifikace), TS 29.561 (5G systém; Interworking mezi 5G sítí a externími datovými sítěmi), TS 29.594 (Konvergence pevných a bezdrátových sítí (WWC) pro 5G systém), TS 31.102 (Aplikace UICC) a TS 43.033 (Zabezpečení pro konvergenci pevných a bezdrátových sítí) definují jeho formát, uložení (např. na UICC) a použití v různých procedurách. Jeho hlavní role spočívá v umožnění páteřní síti rozpoznat konkrétní kontext přístupu přes pevnou linku, což může ovlivnit rozhodnutí o účtování, kvalitě služeb (QoS) a řízení přístupu.

## K čemu slouží

GCI byl zaveden pro podporu konvergence pevných (kabelových) a mobilních sítí, což je trend, který získal významnou dynamiku s 3GPP Release 8 a architekturou EPS. Jak operátoři začali nabízet balené služby, vznikla potřeba bezproblémově autentizovat a poskytovat služby uživatelům bez ohledu na to, zda jsou připojeni přes buněčné rádiové rozhraní nebo přes pevný širokopásmový kabelový modem. Předchozí přístupy postrádaly standardizovaný, globálně jedinečný identifikátor pro kabelové přístupové body, který by mohla mobilní páteřní síť spolehlivě používat pro vazbu zabezpečení a politik. GCI tento problém řeší tím, že poskytuje společný identifikátor, který může být uložen na SIM/USIM karty uživatele (dle TS 31.102) a použit během autentizace, když se zařízení připojuje přes kabelovou síť. To umožňuje operátorům nabízet jednotnou identitu účastníka a konzistentní uživatelský zážitek napříč typy přístupu. Jeho vytvoření bylo motivováno obchodní a technickou snahou směrem ke konvergenci pevných a mobilních sítí ([FMC](/mobilnisite/slovnik/fmc/)) a později ke konvergenci pevných a bezdrátových sítí (WWC), což umožňuje zefektivnění operací, zjednodušení účtování a zvýšení zabezpečení pro scénáře s více přístupy.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor pro kabelový modem nebo koncový bod kabelové sítě
- Může být uložen na UICC (SIM/USIM) pro účely autentizace
- Používán v autentizačních protokolech pro důvěryhodný ne-3GPP přístup k 3GPP páteřním sítím
- Umožňuje přístupově specifické řízení politik a účtování v konvergovaných sítích
- Odkazován ve specifikacích 3GPP pro konvergenci pevných a bezdrátových sítí (WWC)
- Podporuje bezproblémový uživatelský zážitek napříč pevným a mobilním typem přístupu

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 29.594** (Rel-19) — 5G Spending Limit Control Service Stage 3
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 43.033** (Rel-13) — Lawful Interception Stage 2 for GSM/GPRS

---

📖 **Anglický originál a plná specifikace:** [GCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/gci/)
