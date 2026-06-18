---
slug: "rnaa"
url: "/mobilnisite/slovnik/rnaa/"
type: "slovnik"
title: "RNAA – Resource owner-aware Northbound API Access"
date: 2025-01-01
abbr: "RNAA"
fullName: "Resource owner-aware Northbound API Access"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rnaa/"
summary: "Rámec 3GPP pro zabezpečený a autorizovaný přístup třetích stran k síťovým API (např. API NEF), kde jsou volání API obeznámena s politikami koncového uživatele (vlastníka prostředku), jehož data nebo s"
---

RNAA je rámec 3GPP pro zabezpečený a autorizovaný přístup k API, kde jsou volání obeznámena s politikami koncového uživatele, jehož data nebo prostředky jsou přistupovány, a respektují je.

## Popis

Resource owner-aware Northbound [API](/mobilnisite/slovnik/api/) Access (RNAA) je bezpečnostní a autorizační rámec definovaný ve specifikaci 3GPP Release 18 pro architekturu 5G založenou na službách ([SBA](/mobilnisite/slovnik/sba/)). Konkrétně upravuje způsob, jakým poskytovatelé aplikací třetích stran ([AP](/mobilnisite/slovnik/ap/)) nebo vertikály přistupují k funkcím pro vystavení sítě, primárně k funkci Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)), za účelem volání služeb nebo dotazování informací o uživatelském zařízení (UE) či síťovém prostředku. Klíčovou inovací RNAA je, že autorizace pro takový přístup k API není založena pouze na dohodě mezi AP a síťovým operátorem, ale zahrnuje také souhlas a politiky koncového uživatele („vlastníka prostředku“), jehož data nebo síťové schopnosti jsou předmětem požadavku.

Z architektonického hlediska se RNAA týká několika klíčových síťových funkcí ([NF](/mobilnisite/slovnik/nf/)). NEF funguje jako vstupní bod přijímající požadavky API od AP. Rámec zavádí nebo využívá funkce jako Resource Owner-aware Authorization Server (RO-AS), který může být integrován v doméně operátora nebo může být důvěryhodnou externí entitou. Když AP požaduje API, které se týká prostředku uživatele (např. „získat polohu UE-123“), musí NEF ve spolupráci s RO-AS ověřit vícevrstvou autorizační politiku. To zahrnuje kontrolu přihlašovacích údajů AP a smlouvy na úrovni služby, ale také ověření, že vlastník prostředku (uživatel UE-123) udělil souhlas pro tento konkrétní typ přístupu této konkrétní AP, případně s omezeními týkajícími se času, polohy nebo použití dat.

Technický pracovní postup zahrnuje použití standardů OAuth 2.0 a OpenID Connect přizpůsobených pro ekosystém 3GPP. Vlastník prostředku (uživatel) uděluje souhlas prostřednictvím uživatelského rozhraní pro správu souhlasu, což vede k vydání přístupového tokenu vázaného na konkrétní rozsahy (oprávnění API). AP tento token předkládá při volání API NEF. NEF nebo specializovaný bod vynucení politiky ověřuje pravost tokenu, přidružené rozsahy a vazbu na cílový prostředek. Tím se zajišťuje, že volání API nejsou pouze technicky povolena, ale také jsou v souladu s ochranou soukromí a respektují suverenitu uživatele nad jeho osobními údaji a oprávněními síťových služeb. RNAA tak vkládá princip „uživatele v procesu“ do severovýchodního rozhraní sítě.

## K čemu slouží

RNAA byla vytvořena za účelem řešení kritických nedostatků v oblasti ochrany soukromí, zabezpečení a regulatorních požadavků v dřívějších paradigmatech vystavení sítě. Původní severovýchodní [API](/mobilnisite/slovnik/api/), přestože otevírala síťové schopnosti, se primárně spoléhala na binární model důvěry mezi operátorem a poskytovatelem aplikace třetí strany. Tento model nedostatečně zapojoval koncového uživatele, jehož osobní údaje (poloha, stav připojení) nebo síťové prostředky (úprava QoS) byly přistupovány nebo manipulovány. Tato mezera vyvolala významné obavy v rámci předpisů, jako je GDPR, které vyžadují souhlas uživatele se zpracováním dat, a omezila přijetí síťových API pro citlivé případy použití.

Motivace pro RNAA vychází z potřeby umožnit inovativní vertikální aplikace (např. ve zdravotnictví, automobilovém průmyslu nebo chytrých městech), které vyžadují uživatelsky specifické síťové informace nebo kontrolu, a zároveň zajistit soukromí uživatelů a soulad s předpisy. Řeší problém „slepého“ přístupu k API zavedením standardizované, zabezpečené a uživatelem orientované autorizační vrstvy. Před RNAA mohli operátoři implementovat proprietární mechanismy souhlasu, což vytvářelo fragmentaci. RNAA poskytuje jednotný rámec 3GPP, který dává uživatelům kontrolu nad tím, jak jsou jejich síťová data sdílena, buduje důvěru a odemyká nové obchodní modely, kde mohou uživatelé dynamicky udělovat nebo odvolávat přístup aplikacím, což podporuje otevřenější a etičtější digitální ekosystém.

## Klíčové vlastnosti

- Vynucuje souhlas uživatele (vlastníka prostředku) jako předpoklad pro přístup k severovýchodnímu API
- Integruje se s rámci OAuth 2.0/OpenID Connect pro standardizovanou autorizaci
- Poskytuje podrobné řízení přístupu na základě rozsahu pro síťová API (např. poloha, QoS)
- Umožňuje dynamickou správu souhlasu a jeho odvolání koncovým uživatelem
- Spolupracuje s funkcí Network Exposure Function (NEF) jako primární bránou API
- Podporuje soulad s předpisy na ochranu osobních údajů (např. GDPR) při vystavení síťových služeb

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 28.849** (Rel-19) — CAPIF Phase2 Charging Study
- **TS 29.222** (Rel-19) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 33.122** (Rel-19) — Security Architecture for CAPIF
- **TS 33.700** — 3GPP TR 33.700

---

📖 **Anglický originál a plná specifikace:** [RNAA na 3GPP Explorer](https://3gpp-explorer.com/glossary/rnaa/)
