---
slug: "h-udr"
url: "/mobilnisite/slovnik/h-udr/"
type: "slovnik"
title: "H-UDR – Home Unified Data Repository"
date: 2026-01-01
abbr: "H-UDR"
fullName: "Home Unified Data Repository"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/h-udr/"
summary: "Funkce jednotného úložiště dat (UDR) umístěná v domovské veřejné pozemní mobilní síti (HPLMN) uživatele. Ukládá a spravuje předplatitelská data, politiky a aplikační data, která jsou považována za 'do"
---

H-UDR je funkce jednotného úložiště dat (Unified Data Repository) umístěná v domovské síti uživatele, která ukládá a spravuje domovská předplatitelská data, politiky a aplikační data, jako jsou uživatelské profily a nastavení služeb.

## Popis

Domovské jednotné úložiště dat (H-UDR) je funkce jádra sítě v rámci systému 5G (5GS) a evolučně je použitelné i pro 4G Evolved Packet Core (EPC). Zavedené ve specifikaci 3GPP Release 15 jako součást širšího konceptu jednotného úložiště dat ([UDR](/mobilnisite/slovnik/udr/)) se konkrétně vztahuje k instanci UDR umístěné v domovské veřejné pozemní mobilní síti ([HPLMN](/mobilnisite/slovnik/hplmn/)) předplatitele. Samotné UDR je konvergovaná funkce pro ukládání dat navržená k uchovávání předplatitelských dat, dat politik, aplikačních dat a strukturovaných dat pro vystavení v jediném jednotném úložišti, které nahrazuje oddělená úložiště dat předchozích architektur, jako jsou databáze Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) a Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)).

Architektonicky je H-UDR klíčovým centrálním uzlem ve vrstvě správy dat HPLMN. Poskytuje standardizované rozhraní založené na službách (Nudr) ostatním síťovým funkcím ([NF](/mobilnisite/slovnik/nf/)), které potřebují přistupovat k datům, vytvářet je, aktualizovat nebo mazat. Mezi klíčové konzumenty H-UDR patří domovská správa jednotných dat (H-UDM, řídicí protějšek UDR), domovská funkce řízení politik ([H-PCF](/mobilnisite/slovnik/h-pcf/)), funkce vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)) a funkce výběru síťového řezu ([NSSF](/mobilnisite/slovnik/nssf/)). H-UDR ukládá data strukturovaným, na profily orientovaným způsobem. Například uchovává profil předplatitelských dat uživatele (ke kterým přistupuje UDM), profil dat politik (ke kterým přistupuje PCF) a data specifická pro aplikace (ke kterým přistupuje NEF nebo jiné aplikační funkce).

H-UDR funguje jako trvalé úložiště na pozadí. Když UDM potřebuje získat předplatitelské informace uživatele pro ověření registrační žádosti, dotazuje se na H-UDR prostřednictvím rozhraní založeného na službách Nudr. Podobně H-PCF získává pravidla politik spojená s uživatelem nebo službou z H-UDR. Klíčovou vlastností je nezávislost dat; H-UDR data nezpracovává, pouze je ukládá a poskytuje na základě požadavků autorizovaných konzumních NF. Toto oddělení umožňuje nezávislou škálovatelnost úložných a logických funkcí. Data jsou organizována do datových sad (např. předplatitelská data, data politik, aplikační data) a přístup je řízen na základě identity dotazující se NF a podmnožiny dat, ke které je oprávněna číst nebo je upravovat.

Jeho role v síti je zásadní pro poskytování služeb a vymáhání politik. Centralizací 'domovských' dat v HPLMN zajišťuje jediný zdroj pravdy pro předplatitelské profily, politiky služeb a aplikační kontext. To je obzvláště důležité v scénářích roamingu. Když uživatel roamuje, navštívená síť (VPLMN) přistupuje k informacím o politikách a předplatném prostřednictvím mezisíťových rozhraní (např. N8 mezi V-UDM a H-UDM, které následně získávají data z H-UDR). H-UDR umožňuje konzistentní uživatelský zážitek napříč sítěmi, podporuje síťové řezy tím, že ukládá politiky výběru řezů a usnadňuje vystavení aplikací bezpečným ukládáním aplikačních dat, k nimž mohou oprávněné třetí strany přistupovat prostřednictvím NEF.

## K čemu slouží

H-UDR bylo vytvořeno jako součást přechodu jádra 5G sítě na cloud-nativní, na službách založenou architekturu (SBA). Před 5G byla předplatitelská a politická data uložena v oddělených monolitických síťových prvcích, jako je HSS (pro ověřování a předplatné) a SPR (Subscriber Profile Repository) nebo interní databáze PCRF (pro politiky). Tento izolovaný přístup vedl k duplikaci dat, problémům s konzistencí, složité integraci a omezené flexibilitě pro zavádění nových služeb vyžadujících kombinované datové sady. Koncept UDR si kladl za cíl toto úložiště sjednotit.

Označení 'Domovské' u H-UDR řeší konkrétní potřebu centralizovaného, autoritativního datového úložiště v domovské síti předplatitele. Ve scénářích roamingu a vícečetných sítí je nezbytné, aby hlavní kopie předplatitelského profilu, politik a dat služeb sídlila v HPLMN a byla jí řízena. H-UDR řeší problém suverenity a konzistence dat. Zajišťuje, že jakákoli síť (navštívená nebo domovská), která činí rozhodnutí o službě uživatele, čerpá tyto politiky ze stejného zdroje, čímž předchází konfliktům a umožňuje jednotné poskytování služeb globálně. Také zjednodušuje architekturu správy dat pro domovského operátora konsolidací úložiště.

Dále H-UDR umožňuje nové paradigmy 5G, jako jsou síťové řezy a edge computing. Politiky výběru řezů a parametry specifické pro služby mohou být uloženy jako součást uživatelského profilu v H-UDR. Když se UE připojí, UDM a NSSF se mohou dotázat tohoto centralizovaného úložiště, aby určily vhodnou instanci síťového řezu. Pro edge computing mohou být aplikační kontext a preference uloženy v H-UDR a vystaveny edge aplikačním funkcím prostřednictvím NEF. H-UDR tedy není pouze evolucí starších databází, ale základním prvkem umožňujícím flexibilní, na služby reagující sítě 5G, které řeší omezení fragmentovaného ukládání dat v předchozích generacích.

## Klíčové vlastnosti

- Centralizované úložiště pro předplatitelská data, politiky a aplikační data v HPLMN
- Poskytuje rozhraní založené na službách (Nudr) pro přístup ze strany UDM, PCF, NEF a dalších NF
- Organizuje data do oddělených datových sad pro řízení přístupu a správu
- Slouží jako jediný zdroj pravdy pro profily uživatelů a politiky domovské sítě
- Umožňuje konzistentní vymáhání politik a uživatelský zážitek při roamingu
- Podporuje síťové řezy ukládáním dat pro výběr řezů a profilů služeb

## Související pojmy

- [UDR – Unified Data Repository](/mobilnisite/slovnik/udr/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework

---

📖 **Anglický originál a plná specifikace:** [H-UDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/h-udr/)
