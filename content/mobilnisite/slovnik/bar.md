---
slug: "bar"
url: "/mobilnisite/slovnik/bar/"
type: "slovnik"
title: "BAR – Base Avatar Repository"
date: 2026-01-01
abbr: "BAR"
fullName: "Base Avatar Repository"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bar/"
summary: "Base Avatar Repository (BAR) je síťová funkce zavedená ve specifikaci 3GPP Release 14 pro ukládání a správu digitálních avatarů uživatelů. Umožňuje konzistentní reprezentaci avatarů napříč různými slu"
---

BAR je síťová funkce, která ukládá a spravuje digitální avatary uživatelů, aby umožnila jejich konzistentní reprezentaci napříč různými službami, a podporuje tak imerzivní komunikaci jako AR/VR.

## Popis

Base Avatar Repository (BAR) je standardizovaná síťová funkce definovaná v rámci architektury 3GPP, určená speciálně pro správu digitálních avatarů uživatelů. Avatar je digitální reprezentace uživatele, která může sahat od jednoduchého statického obrázku po komplexní animovaný 3D model schopný vyjadřovat emoce a gesta. BAR slouží jako centrální, autoritativní úložiště těchto avatarových assetů a jejich přidružených metadat. Jeho primární rolí je zajistit, aby byl avatar uživatele konzistentní, přenositelný a bezpečně dostupný napříč různými poskytovateli služeb, aplikacemi a zařízeními, což je klíčovým prvkem pro personalizované a imerzivní komunikační služby.

Z architektonického hlediska je BAR typicky implementován jako aplikační server v rámci Service-Based Architecture (SBA) sítí 5G, který své schopnosti zpřístupňuje prostřednictvím standardizovaných rozhraní založených na službách (např. Nbarf), jak je definováno v TS 29.244. Interaguje s dalšími síťovými funkcemi, jako je Unified Data Repository (UDR) pro propojení s uživatelským profilem a funkcemi řízení politik pro autorizaci služeb. Úložiště ukládá více komponent: základní data avatarového modelu (geometrie, textury), informace o riggingu pro animaci, předdefinované animace nebo výrazy a uživatelsky specifické parametry přizpůsobení. Toto strukturované úložiště umožňuje efektivní načítání a vykreslování klientskými aplikacemi.

Provoz BAR zahrnuje několik klíčových procedur. Při zřizování avataru může uživatel nebo autorizovaná aplikace nahrávat, aktualizovat nebo mazat avatarové assety prostřednictvím zabezpečených [API](/mobilnisite/slovnik/api/) volání. BAR tato provádění validuje vůči uživatelským politikám a úložným kvótám. Při využívání avataru, když služba (např. hovor ve rozšířené realitě) vyžaduje avatar uživatele, odešle požadavek na BAR. BAR následně načte příslušné avatarové assety, případně aplikuje transkódování formátu nebo úpravy úrovně detailnosti (LOD) na základě schopností klienta, který o ně žádá (např. mobilní zařízení vs. VR headset). Také řeší správu verzí pro řízení aktualizací a zajištění zpětné kompatibility.

Kritickým technickým aspektem je podpora interoperability ze strany BAR. Poskytnutím standardizovaného úložiště řeší problém fragmentace avatarů, kdy každá služba používá svůj vlastní proprietární formát. BAR může ukládat avatary ve standardizovaných nebo běžně interoperabilních formátech, což usnadňuje jejich použití napříč různými ekosystémy. Dále hraje zásadní roli v řízení soukromí a souhlasu. BAR sám avatary nevykresluje, ale poskytuje data autorizovaným subjektům a vynucuje politiky týkající se toho, kdo má přístup ke kterým atributům avataru. Tato centralizovaná kontrola je nezbytná pro důvěru uživatelů a umožňuje jednotlivcům spravovat, jak je jejich digitální podoba používána napříč více imerzivními službami v síti 5G.

## K čemu slouží

BAR byl vytvořen, aby řešil vznikající potřebu trvalých, uživatelem řízených digitálních identit v komunikačních sítích nové generace. Před jeho standardizací byla data avatarů typicky uzavřena v rámci jednotlivých aplikací nebo her. Tento nedostatek přenositelnosti znamenal, že uživatelé museli svou digitální podobu vytvářet znovu pro každou novou službu, což vedlo ke špatné uživatelské zkušenosti a fragmentaci. Vzestup imerzivních služeb jako komunikace ve rozšířené realitě ([AR](/mobilnisite/slovnik/ar/)), virtuální realitě (VR) a rozšířené realitě (XR) v sítích 5G si vyžádal síťové řešení pro spolehlivou správu těchto složitých digitálních assetů ve velkém měřítku.

Primární problém, který BAR řeší, je oddělení základní digitální identity uživatele (jeho avataru) od jakékoli jednotlivé aplikace nebo poskytovatele služeb. To umožňuje model 'napsat jednou, použít kdekoliv' pro avatary, který je zásadní pro vizi metavesmíru a bezproblémových zážitků napříč službami. Také řeší technické výzvy v imerzivní komunikaci, jako je potřeba nízkolatenčního přístupu k vysoce kvalitním datům avatarů během interakcí v reálném čase a efektivní distribuce těchto dat napříč různorodou škálou zařízení (od telefonů po VR headset).

Historicky byla správa avatarů záležitostí aplikační vrstvy bez podpory sítě. Omezení tohoto přístupu se stala zřejmými s nasazením sítí 5G a jejich schopností enhanced Mobile Broadband (eMBB) a massive Machine-Type Communication (mMTC), které jsou předpokladem pro rozšířené XR. 3GPP uznalo, že pro úspěch těchto služeb musí síť sama poskytovat společné podpůrné prvky. BAR, zavedený v Release 14 jako součást studie o podpůrných prvcích pro služby imerzivní teleprezence, poskytuje tuto základní schopnost. Umožňuje síťovým operátorům nabízet avatar jako službu, čímž vytváří nové obchodní modely a zároveň prostřednictvím standardizace zajišťuje soukromí uživatelů, bezpečnost dat a interoperabilitu.

## Klíčové vlastnosti

- Centralizované úložiště a správa avatarových assetů a metadat uživatele
- Standardizovaná rozhraní založená na službách (např. Nbarf) pro síťovou integraci
- Podpora správy verzí avatarů, transkódování a úprav úrovně detailnosti
- Vynucování politik pro řízení přístupu a správu souhlasu uživatele
- Interoperabilita prostřednictvím podpory běžných formátů avatarových modelů
- Integrace se síťovými funkcemi jádra 5G, jako je UDR, pro asociaci s uživatelským profilem

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 26.264** (Rel-19) — IMS-based AR Real-Time Communication
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 33.790** (Rel-19) — Security for Next-Gen Real-Time Communication Phase 2

---

📖 **Anglický originál a plná specifikace:** [BAR na 3GPP Explorer](https://3gpp-explorer.com/glossary/bar/)
