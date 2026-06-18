---
slug: "bsg"
url: "/mobilnisite/slovnik/bsg/"
type: "slovnik"
title: "BSG – Basic Service Group"
date: 2025-01-01
abbr: "BSG"
fullName: "Basic Service Group"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bsg/"
summary: "Logické seskupení základních telekomunikačních služeb definované ve standardech 3GPP pro účely správy služeb a účtování. Umožňuje operátorům kategorizovat a spravovat základní komunikační schopnosti,"
---

BSG je logické seskupení základních telekomunikačních služeb, jako jsou hlasové hovory nebo SMS, definované 3GPP pro správu operátora, účtování a řízení politik.

## Popis

Základní skupina služeb (Basic Service Group – BSG) je základní koncept správy služeb v sítích 3GPP, který poskytuje logický rámec pro seskupení příbuzných základních telekomunikačních služeb. Základní služba představuje jednotlivou komunikační schopnost, kterou síť poskytuje účastníkům, jako je telefonie, tísňová volání, služba krátkých zpráv ([SMS](/mobilnisite/slovnik/sms/)), fax nebo různé datové přenosové služby. BSG organizuje tyto jednotlivé služby do logických kolekcí, které lze spravovat, provozovat a účtovat jako ucelené entity.

Architektonicky BSG fungují v rámci servisní vrstvy sítí 3GPP a rozhraní s prvky jádra sítě i s podnikovými podpůrnými systémy ([BSS](/mobilnisite/slovnik/bss/)). Koncept je implementován prostřednictvím servisních profilů uložených v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), které obsahují předplatitelská data včetně BSG, ke kterým má účastník přístup. Když účastník zahájí žádost o službu, síť před jejím povolením zkontroluje, zda požadovaná základní služba patří do autorizované BSG v profilu účastníka.

Z provozního hlediska BSG umožňují diferenciaci služeb a detailní kontrolu nad tím, ke kterým službám mohou účastníci přistupovat. Každá BSG může obsahovat více základních služeb, které sdílejí společné charakteristiky nebo jsou typicky používány společně. Například BSG 'Hlasové služby' může zahrnovat telefonii, tísňová volání a služby skupinových hlasových hovorů, zatímco BSG 'Služby zasílání zpráv' může zahrnovat SMS, rozšířené zasílání zpráv a služby multimediálních zpráv. Toto seskupení zjednodušuje správu služeb tím, že umožňuje operátorům povolit nebo zakázat celé kategorie služeb jedinou změnou konfigurace namísto úpravy oprávnění jednotlivých služeb.

Rámec BSG hraje klíčovou roli v systémech účtování a fakturace, kde lze na základě členství v BSG uplatňovat různé tarifní struktury. Účtovací systémy mohou uplatňovat specifická pravidla tarifikace na všechny služby v rámci BSG, což umožňuje modelování svázaných cen a propagačních nabídek. Kromě toho BSG podporují funkci zákazu služeb, což umožňuje operátorům dočasně nebo trvale omezit přístup k celým skupinám služeb z důvodů, jako je nezaplacení, prevence podvodů nebo dodržování regulatorních požadavků. Koncept zůstává relevantní napříč více vydáními 3GPP, protože poskytuje stabilní základ pro správu služeb, který se přizpůsobuje vyvíjejícím se síťovým schopnostem.

## K čemu slouží

Koncept Základní skupiny služeb byl zaveden, aby řešil rostoucí složitost správy služeb v mobilních sítích, jak se vyvíjely za hranice jednoduché hlasové telefonie. Rané buněčné systémy nabízely omezené služby, ale se zavedením sítí 2,5G a 3G potřebovali operátoři spravovat rozmanité portfolia služeb včetně [SMS](/mobilnisite/slovnik/sms/), datových služeb, multimediálních zpráv a různých přidaných služeb. Bez mechanismu seskupování by každá služba vyžadovala individuální konfiguraci v profilech účastníků, což by vedlo k administrativní složitosti a potenciálním nekonzistencím.

BSG tento problém řeší tím, že poskytují logickou abstraktní vrstvu, která zjednodušuje provozování, správu a účtování služeb. Umožňují operátorům vytvářet balíčky služeb, které lze snadno přiřadit účastníkům, a snižují tak provozní náročnost spojenou se správou oprávnění jednotlivých služeb. To je obzvláště důležité pro systémy předplacených služeb a účtování v reálném čase, kde musí být rozhodnutí o autorizaci služby provedena rychle během sestavování hovoru nebo zahájení relace.

Koncept také řeší potřebu flexibilního svazování služeb a tarifních struktur na konkurenčních telekomunikačních trzích. Seskupením příbuzných služeb mohou operátoři vytvářet atraktivní balíčky služeb pro různé zákaznické segmenty, implementovat rodinné tarify a nabízet propagační balíčky. Z technického hlediska BSG poskytují standardizovaný způsob, jak implementovat zákaz služeb napříč více příbuznými službami současně, což je nezbytné pro správu podvodů, řízení kreditu a regulatorní požadavky, jako jsou možnosti zákonného odposlechu.

## Klíčové vlastnosti

- Logické seskupení příbuzných základních telekomunikačních služeb
- Zjednodušené provozování služeb prostřednictvím svázané správy služeb
- Integrovaná podpora účtování a fakturace pro skupiny služeb
- Možnosti zákazu služeb na úrovni skupiny
- Standardizované rozhraní s HLR/HSS pro správu předplatného
- Podpora autorizace služeb v reálném čase během sestavování hovoru/relace

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.016** (Rel-19) — Subscriber Data Management Stage 2
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [BSG na 3GPP Explorer](https://3gpp-explorer.com/glossary/bsg/)
