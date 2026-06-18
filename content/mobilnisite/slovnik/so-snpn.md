---
slug: "so-snpn"
url: "/mobilnisite/slovnik/so-snpn/"
type: "slovnik"
title: "SO-SNPN – Subscription Owner Standalone Non-Public Network"
date: 2026-01-01
abbr: "SO-SNPN"
fullName: "Subscription Owner Standalone Non-Public Network"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/so-snpn/"
summary: "Samostatná neveřejná síť (SNPN), kde správu předplatného a jeho vlastnictví zajišťuje sám provozovatel SNPN, nikoli operátor veřejné mobilní sítě (PLMN). Umožňuje plně privátní 5G sítě s nezávislou sp"
---

SO-SNPN je samostatná neveřejná síť (Standalone Non-Public Network), kde provozovatel sítě nezávisle spravuje a vlastní předplatné, namísto spoléhání se na operátora veřejné mobilní sítě.

## Popis

Subscription Owner Standalone Non-Public Network (SO-SNPN) je specifický operační model pro 5G neveřejnou síť ([NPN](/mobilnisite/slovnik/npn/)), jak je definován ve 3GPP Release 17 a novějších. V tomto modelu je síť samostatnou NPN ([SNPN](/mobilnisite/slovnik/snpn/)), což znamená, že funguje nezávisle bez nutnosti využívat síťové funkce veřejné pozemní mobilní sítě ([PLMN](/mobilnisite/slovnik/plmn/)). Klíčovým odlišujícím znakem SO-SNPN je, že subjekt, který provozuje SNPN, zároveň vystupuje jako 'vlastník předplatného' (Subscription Owner) – tedy autorita, která vydává a spravuje identity předplatitelů a jejich přihlašovací údaje. To je v protikladu k SNPN, která spoléhá na přihlašovací údaje od PLMN (konceptuálně podobné roamingu).

Z architektonického hlediska se SO-SNPN skládá ze všech standardních síťových funkcí 5G jádra ([AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/), [UDM](/mobilnisite/slovnik/udm/), [AUSF](/mobilnisite/slovnik/ausf/) atd.) a rádiového přístupu, které jsou však vyhrazeny pro privátní síť. Kritickou součástí je funkce Unified Data Management (UDM) a Authentication Server Function (AUSF), které jsou nakonfigurovány s daty předplatitelů vlastněnými a spravovanými samotným provozovatelem SNPN. Když se uživatelské zařízení (UE) pokouší přistoupit k SO-SNPN, použije identifikátor předplatitele specifický pro tuto privátní síť. Primárním identifikátorem je identifikátor sítě ([NID](/mobilnisite/slovnik/nid/)) kombinovaný s PLMN ID, které je speciálně přiděleno pro použití v SNPN (nejedná se o komerční PLMN ID). UE se přímo autentizuje s AUSF/UDM SO-SNPN pomocí přihlašovacích údajů uložených na své univerzální integrované obvodové kartě (UICC) nebo v úložišti softwarových přihlašovacích údajů, které zřídil provozovatel SNPN.

Fungování zahrnuje vyhrazený postup registrace a autentizace. UE identifikuje dostupné SNPN podle vysílaného NID a SNPN PLMN ID. Pro přístup k SO-SNPN musí UE mít předplatné konkrétně pro tuto síť. Během počáteční registrace UE poskytne svůj SUCI (Subscription Concealed Identifier) odvozený od svého předplatného specifického pro SNPN. Síťové funkce SO-SNPN tento požadavek zpracují interně. AUSF provede autentizaci s UDM pomocí přihlašovacích údajů vlastněných provozovatelem SNPN a vytvoří bezpečnostní kontext bez jakékoli interakce s domácím systémem předplatitelů externí veřejné sítě. Tento model dává provozovateli privátní sítě úplnou autonomii nad správou životního cyklu předplatitelů, bezpečnostními politikami a poskytováním služeb ve své izolované doméně.

## K čemu slouží

Koncept SO-SNPN byl vytvořen, aby vyhověl poptávce vertikálních odvětví (např. továren, přístavů, energetiky, kampusů) po skutečně privátních a autonomních 5G sítích. Před Release 17 koncepty privátních sítí často zahrnovaly určitou závislost na operátorech veřejných mobilních sítí, například využití síťového řezání na veřejné PLMN nebo vyžadování přihlašovacích údajů vydaných PLMN pro přístup. Tato závislost mohla být pro odvětví vyžadující plnou kontrolu nad svou síťovou infrastrukturou, suverenitu nad daty, provozní nezávislost a specializované bezpečnostní modely nežádoucí.

SO-SNPN řeší problém úplné provozní separace. Umožňuje podniku nebo vertikálnímu odvětví nasadit 5G síť jako plně soběstačný systém, kde je jedinou autoritou pro vydávání identit svým zaměstnancům, zařízením a senzorům. To je zásadní pro prostředí citlivá na bezpečnost, kde data předplatitelů nesmí opustit areál, pro specializovaná zařízení, která nikdy nebudou potřebovat přístup do veřejné sítě, a pro provozní modely, kde podnik chce být zcela nezávislý na poskytovatelích telekomunikačních služeb. Řeší omezení dřívějších přístupů tím, že poskytuje standardizovanou, 3GPP definovanou metodu pro vybudování privátní buněčné sítě se stejnou úrovní kontroly jako u tradiční Wi-Fi nebo kabelové podnikové sítě, ale s vynikajícím výkonem, spolehlivostí a funkcemi mobility 5G NR. To umožňuje vertikálním odvětvím přizpůsobit síť přesně jejich jedinečným požadavkům aplikací a bezpečnosti.

## Klíčové vlastnosti

- Plné vlastnictví a správa identit předplatitelů provozovatelem SNPN
- Funguje s vyhrazeným identifikátorem SNPN (NID + SNPN PLMN ID)
- Nezávislá autentizace pomocí přihlašovacích údajů vlastněných SNPN (např. na UICC)
- Žádná technická závislost na operátorovi veřejné mobilní sítě (PLMN)
- Úplná kontrola nad životním cyklem předplatitelů a přístupovými politikami
- Umožňuje izolovaný provoz pro zvýšenou bezpečnost a suverenitu nad daty

## Související pojmy

- [SNPN – Standalone Non-Public Network](/mobilnisite/slovnik/snpn/)
- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks

---

📖 **Anglický originál a plná specifikace:** [SO-SNPN na 3GPP Explorer](https://3gpp-explorer.com/glossary/so-snpn/)
