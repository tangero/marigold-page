---
slug: "cdp"
url: "/mobilnisite/slovnik/cdp/"
type: "slovnik"
title: "CDP – Charging Determination Point"
date: 2026-01-01
abbr: "CDP"
fullName: "Charging Determination Point"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cdp/"
summary: "Charging Determination Point (CDP) je funkční entita v architektuře účtování 3GPP odpovědná za shromažďování účtovacích informací od síťových funkcí a určování odpovídajících účtovacích událostí. Slou"
---

CDP je funkční entita v architektuře účtování 3GPP, která shromažďuje účtovací informace, určuje účtovací události a uplatňuje účtovací pravidla před předáním dat pro offline nebo online účtování.

## Popis

Charging Determination Point (CDP) je kritická funkční komponenta v architektuře účtování 3GPP, konkrétně definovaná v rámci frameworku Policy and Charging Control (PCC). Funguje jako zprostředkovatel mezi síťovými funkcemi, které generují data o využití (jako PCEF nebo TDF), a backendovými účtovacími systémy, které tato data zpracovávají pro účely fakturace. Primární funkcí CDP je přijímat nezpracované účtovací události od různých síťových prvků, uplatňovat účtovací pravidla a politiky k určení odpovídajícího účtovacího zacházení a následně předávat tyto standardizované záznamy účtovacích dat ([CDR](/mobilnisite/slovnik/cdr/)) příslušnému účtovacímu systému.

Architektonicky je CDP typicky implementován jako součást nebo v úzké součinnosti s funkcí Policy and Charging Rules Function (PCRF). Přijímá účtovací informace přes referenční bod Gx od Policy and Charging Enforcement Function (PCEF) a přes referenční bod Sd od Traffic Detection Function (TDF). CDP zpracovává tyto události podle politik přijatých od PCRF, které zahrnují filtry datových toků služeb, účtovací klíče, ratingové skupiny a další parametry určující, jak má být účtováno konkrétní síťové využití. Toto zpracování zahrnuje korelaci více účtovacích událostí, uplatňování prahových hodnot založených na čase nebo objemu a rozhodování o tom, kdy generovat průběžné nebo konečné účtovací záznamy.

Fungování CDP zahrnuje několik klíčových technických procesů. Nejprve přijímá Charging Events ([CE](/mobilnisite/slovnik/ce/)) od síťových funkcí, které obsahují informace o uživatelských relacích, objemech dat, využití služeb a dalších měřitelných parametrech. CDP poté porovnává tyto události s aktivními pravidly politik, aby určil odpovídající účtovací zacházení. Tento proces porovnávání bere v úvahu faktory jako uživatelský profil předplatného, charakteristiky služby, síťové podmínky a obchodní pravidla definovaná operátorem. Po přiřazení CDP uplatňuje účtovací parametry, jako jsou ratingové skupiny (které se mapují na konkrétní tarifní sazby) a účtovací klíče (které identifikují službu nebo obsah, za který se účtuje).

Po zpracování CDP generuje standardizované Charging Data Records (CDR) nebo Charging Events Records ([CER](/mobilnisite/slovnik/cer/)), které obsahují všechny potřebné informace pro fakturaci. Tyto záznamy zahrnují časová razítka, identifikátory uživatele, identifikátory služeb, množství využití, účtovací parametry a další metadata vyžadovaná pro přesné účtování. CDP poté předává tyto záznamy příslušnému účtovacímu systému: funkci Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)) přes referenční bod Ga pro offline účtování (post-paid fakturace), nebo Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) přes referenční bod Gy pro online účtování (pre-paid nebo řízení kreditu v reálném čase). Toto oddělení zajišťuje, že účtovací logika je centralizovaná a konzistentní bez ohledu na fakturační model.

CDP hraje v síti několik důležitých rolí nad rámec základního určování účtování. Umožňuje účtování s ohledem na službu tím, že rozlišuje mezi různými typy provozu a uplatňuje odpovídající účtovací pravidla. Podporuje konvergované účtování napříč více přístupovými technologiemi (2G, 3G, 4G, 5G) poskytováním jednotného účtovacího rozhraní. Usnadňuje účtování řízené politikami, kde mohou být fakturační pravidla dynamicky upravována na základě síťových podmínek, chování uživatele nebo propagačních nabídek. Dále CDP poskytuje schopnosti korelace účtování, což operátorům umožňuje kombinovat účtovací události z více zdrojů (hlas, data, zprávy, služby s přidanou hodnotou) do souvislých fakturačních záznamů pro každou uživatelskou relaci.

## K čemu slouží

Charging Determination Point byl vytvořen, aby řešil rostoucí složitost účtování v moderních mobilních sítích. Jak se sítě 3GPP vyvíjely od jednoduchých hlasových služeb k bohatým multimediálním a datovým službám, tradiční přístupy k účtování se staly nedostatečnými. Dřívější účtovací systémy obvykle přijímaly nezpracovaná data o využití přímo od síťových prvků bez mezilehlého zpracování, což vedlo k nekonzistentnostem, složitým požadavkům na integraci a omezené flexibilitě v uplatňování účtovacích pravidel. Operátoři potřebovali sofistikovanější mechanismus pro konzistentní uplatňování složitých účtovacích politik napříč různými síťovými funkcemi a službami.

CDP byl zaveden konkrétně za účelem oddělení logiky určování účtování od jak vymáhacích funkcí (které zpracovávají provoz), tak fakturačních funkcí (které zpracovávají záznamy). Toto architektonické oddělení umožňuje operátorům implementovat složitá účtovací pravidla bez nutnosti modifikace každého síťového prvku. Umožňuje účtování s ohledem na službu, kde mohou být různé typy provozu (streamované video, prohlížení webu, IoT data) účtovány odlišně na základě obsahu, kvality nebo obchodních dohod. CDP také řeší potřebu schopností účtování v reálném čase vyžadovaných pro pre-paid služby a kontroly výdajových limitů, poskytuje standardizované rozhraní mezi síťovým využitím a systémy správy kreditu.

Dále CDP řeší problém korelace účtování v prostředí s více službami. Moderní uživatelé současně využívají hlas, data, zprávy a různé služby s přidanou hodnotou, často v rámci stejné relace. CDP poskytuje inteligenci ke korelaci těchto různorodých účtovacích událostí do souvislých fakturačních záznamů. Také umožňuje účtování řízené politikami, kde může být fakturace dynamicky upravována na základě síťových podmínek (jako je vytížení), chování uživatele (jako je roamingový status) nebo obchodních pravidel (jako jsou propagační nabídky). Tato flexibilita se stala nezbytnou, když operátoři přecházeli od jednoduchého účtování za minutu nebo za megabajt ke složitým vrstveným tarifům, balíčkovým službám a modelům účtování založeným na kvalitě.

## Klíčové vlastnosti

- Centralizované zpracování účtovacích událostí z více síťových funkcí
- Uplatňování dynamických účtovacích pravidel a politik přijatých od PCRF
- Generování standardizovaných Charging Data Records (CDR) pro fakturační systémy
- Podpora rozhraní pro offline (post-paid) i online (v reálném čase) účtování
- Rozlišení účtování s ohledem na službu na základě typu provozu a obsahu
- Korelace účtování napříč více službami v rámci uživatelských relací

## Související pojmy

- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [CDF – Cumulative Distribution Function](/mobilnisite/slovnik/cdf/)

## Definující specifikace

- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.458** (Rel-8) — SIP Transfer of Tariff Info for Charging
- **TS 29.658** (Rel-19) — SIP Transfer of Tariff Information
- **TS 32.280** (Rel-19) — Advice of Charge (AoC) Framework
- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements

---

📖 **Anglický originál a plná specifikace:** [CDP na 3GPP Explorer](https://3gpp-explorer.com/glossary/cdp/)
