---
slug: "smaf"
url: "/mobilnisite/slovnik/smaf/"
type: "slovnik"
title: "SMAF – Service Management Agent Function"
date: 2025-01-01
abbr: "SMAF"
fullName: "Service Management Agent Function"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/smaf/"
summary: "SMAF je standardizovaná funkce v rámci bezpečnostní architektury 3GPP, která poskytuje zabezpečené rozhraní pro externí poskytovatele služeb ke správě jejich služeb v mobilní síti. Funguje jako důvěry"
---

SMAF je standardizovaná bezpečnostní funkce, která poskytuje zabezpečené rozhraní pro externí poskytovatele služeb ke správě jejich služeb v mobilní síti, přičemž funguje jako důvěryhodný agent pro autorizaci operací.

## Popis

Service Management Agent Function (SMAF) je klíčová komponenta definovaná v dokumentu 3GPP TS 33.108, který specifikuje bezpečnostní rámec pro správu služeb třetích stran. Z architektonického hlediska se SMAF nachází v důvěryhodné doméně mobilního síťového operátora ([MNO](/mobilnisite/slovnik/mno/)) a slouží jako zabezpečená brána nebo proxy mezi externími poskytovateli služeb a interními správními systémy sítě. Jejím primárním úkolem je ověřovat a autorizovat požadavky na správu služeb pocházející z vnějšku administrativní domény operátora, přičemž tyto požadavky překládá a předává příslušným síťovým funkcím nebo servisním platformám. Tím je zajištěno zachování jasné bezpečnostní hranice.

Při své činnosti SMAF implementuje robustní sadu bezpečnostních protokolů pro zpracování komunikace související se správou služeb. Když externí subjekt, například poskytovatel služeb s přidanou hodnotou, potřebuje zřídit, nakonfigurovat nebo monitorovat službu hostovanou v mobilní síti, odešle správní požadavek na SMAF. SMAF nejprve ověří původ požadavku pomocí robustních autentizačních mechanismů, zkontroluje autorizační práva poskytovatele služeb vůči databázi politik a poté aplikuje případné nezbytné bezpečnostní transformace (jako je dešifrování nebo ověření integrity). Teprve po úspěšném absolvování těchto bezpečnostních kontrol předává SMAF legitimní požadavek interní Service Management Function ([SMF](/mobilnisite/slovnik/smf/)) nebo jinému relevantnímu síťovému prvku k provedení.

Interní komponenty SMAF typicky zahrnují zabezpečené komunikační rozhraní (často založené na [TLS](/mobilnisite/slovnik/tls/)/[SSL](/mobilnisite/slovnik/ssl/)), motor pro ověřování a autorizaci, bod pro vynucování politik a moduly pro logování/audit. Její role je klíčová pro umožnění zabezpečené expozice a správy služeb, což je základním kamenem moderních modelů typu síť-jako-sluzba a partnerství. Díky centralizaci a standardizaci bezpečnostního zpracování pro externí správu SMAF brání přímému, potenciálně zranitelnému přístupu k rozhraním správy jádra sítě, čímž výrazně snižuje útočnou plochu a zajišťuje soulad s bezpečnostními politikami operátora.

## K čemu slouží

SMAF byla zavedena, aby řešila rostoucí potřebu mobilních síťových operátorů bezpečně otevírat své sítě poskytovatelům služeb třetích stran. Historicky byla správa služeb uzavřenou interní operací. Jak se mobilní sítě vyvíjely v platformy pro rozsáhlý ekosystém služeb (jako jsou zasílání zpráv, služby založené na poloze a IoT), stala se nezbytnou bezpečná a standardizovaná metoda, která umožní externím subjektům spravovat jejich vlastní služby. SMAF řeší problém, jak poskytnout nezbytný správní přístup, aniž by byla ohrožena bezpečnost a integrita jádra sítě.

K jejímu vytvoření vedly omezení ad-hoc proprietárních rozhraní, která byla nebezpečná, obtížně auditovatelná a neškálovatelná. Bez funkce jako je SMAF by operátoři museli přímo vystavovat interní správní rozhraní, což by vytvářelo obrovská bezpečnostní rizika, nebo vyvíjet vlastní, jednorázová řešení pro každého partnera, což je neefektivní a náchylné k chybám. SMAF poskytuje jednotnou, standardy založenou bezpečnostní vrstvu, která umožňuje obchodní inovace prostřednictvím partnerství, a zároveň zachovává přísnou provozní kontrolu a bezpečnostní záruky. Tvoří klíčovou část bezpečnostní architektury 3GPP pro správu sítě a zajišťuje, že rozšiřování nabídky služeb neprobíhá na úkor zranitelnosti sítě.

## Klíčové vlastnosti

- Zabezpečená brána pro přístup externí správy služeb
- Robustní ověřování a autorizace externích poskytovatelů služeb
- Vynucování politik pro operace správy služeb
- Bezpečnostní hranice mezi externími a interními síťovými doménami
- Standardizované rozhraní dle 3GPP TS 33.108
- Auditování a logování všech externích správních transakcí

## Definující specifikace

- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [SMAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/smaf/)
