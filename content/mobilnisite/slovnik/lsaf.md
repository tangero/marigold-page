---
slug: "lsaf"
url: "/mobilnisite/slovnik/lsaf/"
type: "slovnik"
title: "LSAF – Location Subscriber Authorization Function"
date: 2025-01-01
abbr: "LSAF"
fullName: "Location Subscriber Authorization Function"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lsaf/"
summary: "Funkce jádra sítě zodpovědná za autorizaci požadavků na službu polohy pro cílového mobilního účastníka. Ověřuje právní a soukromá práva žádající entity (např. aplikace nebo jiného síťového uzlu) na zí"
---

LSAF je funkce jádra sítě, která autorizuje požadavky na službu polohy ověřením právních a soukromých práv entity na získání polohových informací účastníka.

## Popis

Location Subscriber Authorization Function (LSAF) je kritická bezpečnostní a soukromí chránící komponenta v architektuře služby polohy ([LCS](/mobilnisite/slovnik/lcs/)) 3GPP. Funguje jako rozhodovací bod politik pro polohové požadavky a zajišťuje, že každý pokus o lokalizaci uživatelského zařízení (UE) je v souladu s nastavením soukromí účastníka, síťovými politikami a platnými právními předpisy. LSAF je typicky implementována jako logická funkce uvnitř Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) nebo jako samostatný uzel s tímto rozhraním. Když klient služby polohy (LCS) – což může být externí aplikace, služba s přidanou hodnotou nebo interní síťová entita jako [MSC](/mobilnisite/slovnik/msc/) pro tísňová volání – odešle požadavek na polohu do GMLC, GMLC vyvolá LSAF.

Autorizační proces zahrnuje několik klíčových kontrol. Nejprve LSAF ověří identitu a přihlašovací údaje klienta LCS, který žádost podává. Poté načte profil soukromí polohy cílového účastníka ze serveru Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)). Tento profil, definovaný účastníkem, specifikuje, kterým klientům je dovoleno požadovat jeho polohu, za jakých podmínek (např. denní doba) a jaká úroveň přesnosti polohy je povolena. LSAF vyhodnotí aktuální žádost vůči tomuto profilu. Dále LSAF vynucuje síťové politiky a právní požadavky, jako jsou povinnosti lokalizace pro tísňové služby (např. E112 v Evropě), které mohou mít přednost před běžným nastavením soukromí.

Pokud je žádost autorizována, LSAF vrátí GMLC pozitivní výsledek autorizace, který následně pokračuje v zahájení procesu určení polohy s rádiovým přístupovým a jádrovým segmentem sítě. Pokud je žádost zamítnuta, LSAF nařídí GMLC, aby ji odmítl s příslušným kódem chyby. LSAF také hraje roli v procedurách notifikace a verifikace, kde síť může být povinna účastníka informovat, že je o jeho polohu žádáno, a získat jeho souhlas. Centralizací této autorizační logiky LSAF poskytuje konzistentní a auditovatelnou bezpečnostní vrstvu, která chrání soukromí účastníka a zároveň umožňuje fungovat legitimním službám založeným na poloze.

## K čemu slouží

LSAF byla vytvořena, aby řešila zásadní problémy ochrany soukromí a bezpečnosti spojené s určováním a zveřejňováním geografické polohy mobilního účastníka. S nástupem služeb založených na poloze existovalo jasné riziko neautorizovaného sledování a zneužití vysoce citlivých osobních údajů. Rané systémy postrádaly standardizovaný robustní mechanismus pro kontrolu toho, kdo může o polohu žádat a za jakých okolností. LSAF byla zavedena, aby vytvořila formální, standardizovanou autorizační bránu uvnitř síťové architektury.

Jejím účelem je řešit problém nekontrolovaného přístupu k poloze, zajišťovat soulad s rostoucími předpisy na ochranu údajů (jako je směrnice EU o ochraně údajů) a budovat důvěru uživatelů. Poskytuje technické prostředky k implementaci voleb účastníka v oblasti soukromí, přičemž převádí obecná pravidla soukromí na vynutitelná síťová rozhodnutí. Bez LSAF by provozovatelé těžko mohli nabízet komerční polohové služby třetím stranám a zároveň zachovávat soulad s předpisy a chránit své účastníky. LSAF tedy umožnila komerční ekosystém služeb založených na poloze tím, že poskytla nezbytné záruky ochrany soukromí, což provozovatelům umožnilo poskytovat možnosti lokalizace externím poskytovatelům aplikací z hlediska právního i etického.

## Klíčové vlastnosti

- Autorizuje všechny požadavky na službu polohy pro cílového mobilního účastníka
- Vyhodnocuje žádosti vůči profilu soukromí účastníka z HSS/HLR
- Ověřuje identitu a práva žádajícího klienta LCS
- Vynucuje politiky síťového operátora a právní/regulační požadavky
- Podporuje procedury notifikace a verifikace pro souhlas účastníka
- Integruje se s Gateway Mobile Location Centre (GMLC) v architektuře LCS

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [LSAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lsaf/)
