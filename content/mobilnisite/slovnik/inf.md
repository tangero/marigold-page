---
slug: "inf"
url: "/mobilnisite/slovnik/inf/"
type: "slovnik"
title: "INF – INFormation field"
date: 2025-01-01
abbr: "INF"
fullName: "INFormation field"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/inf/"
summary: "INF je pole proměnné délky v určitých datových jednotkách protokolů 3GPP používané k přenosu základních řídicích nebo uživatelských informací. Jeho struktura a interpretace jsou definovány konkrétním"
---

INF je pole proměnné délky v datových jednotkách protokolů 3GPP, které přenáší základní řídicí nebo uživatelské informace a slouží jako základní, flexibilní kontejner pro užitečná data při signalizaci a přenosu dat.

## Popis

Pole INFormation (INF) je obecný kontejner proměnné délky používaný v datových strukturách různých specifikací protokolů 3GPP, jak je uvedeno ve slovníkové specifikaci TS 21.905. Není to samotný protokol, ale základní stavební prvek v rámci definic protokolových zpráv. Pole INF je navrženo tak, aby neslo skutečné podstatné informace potřebné pro konkrétní protokolovou výměnu. Obsah, kódování a sémantika pole INF jsou plně definovány kontextem, ve kterém je použito – konkrétně protokolovou vrstvou a konkrétním typem zprávy (Protocol Discriminator a Message Type), která jej obaluje.

Technicky má datová jednotka protokolu ([PDU](/mobilnisite/slovnik/pdu/)) obsahující pole INF obvykle strukturovanou hlavičku následovanou polem INF. Hlavička obsahuje pevné prvky, jako jsou identifikátory transakcí, rozlišovače protokolů a typy zpráv. Pole INF pak tvoří zbytek PDU. Jeho vnitřní struktura se často skládá z řady informačních prvků (Information Elements – IEs), z nichž každý má svůj vlastní identifikátor, délku a hodnotu. Například v zprávě pro nastavení spojení řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) by pole INF obsahovalo IEs určující rádiové parametry, konfigurace kanálů a identity UE. Síť a UE dekódují pole INF na základě sdílené znalosti specifikace protokolu pro daný konkrétní typ zprávy.

Z architektonického hlediska použití pole INF podporuje efektivitu a rozšiřitelnost protokolu. Díky poli proměnné délky se protokoly vyhýbají plýtvání přenosovou kapacitou pevně dlouhými zprávami, které jsou často vyplněny jen částečně. Důležitější je, že umožňuje zpětně kompatibilní vývoj. Nové IEs lze v pozdější verzi protokolu přidat do pole INF zprávy. Příjemci kompatibilní se starší verzí mohou (pokud to pravidla protokolu umožňují) ignorovat nové, neznámé IEs a stále zpracovat části, kterým rozumějí, pokud zůstane stabilní základní struktura zprávy s kontejnerem INF. Tento vzor je všudypřítomný napříč signalizačními protokoly vrstvy 3 v 3GPP, včetně RRC, Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) a některých protokolů aplikací jádra sítě.

## K čemu slouží

Účelem pole INFormation (INF) je poskytnout standardizovaný, flexibilní mechanismus pro zapouzdření proměnného a vyvíjejícího se obsahu zpráv řídicí roviny v telekomunikačních protokolech. Rané komunikační protokoly někdy používaly zprávy s pevným formátem, které se s rostoucí komplexitou služeb staly neefektivními a nepružnými. Jakýkoli nový parametr vyžadoval nový typ zprávy nebo zásadní změnu formátu zprávy. Koncept pole INF tento problém řeší oddělením identity zprávy (v hlavičce) od obsahu zprávy (v poli INF).

Tento návrh řeší problém dlouhověkosti protokolu a interoperability mezi více dodavateli. Umožňuje, aby základní struktura protokolu – způsob zahájení, potvrzení a rozlišení zpráv – zůstala jednoduchá a stabilní, zatímco podrobné informace potřebné pro bohatou sadu funkcí mohou růst a měnit se uvnitř kontejneru INF. Pro 3GPP, které spravuje standardy používané stovkami dodavatelů zařízení po celém světě, je toto kritické. Umožňuje hladké zavádění nových funkcí (např. nových parametrů QoS, bezpečnostních algoritmů nebo procedur mobility) bez nutnosti kompletní přestavby podkladových stavových automatů protokolu.

Motivací pro jeho formální definici ve slovníkové specifikaci, jako je TS 21.905, je zajistit konzistentní terminologii a porozumění napříč všemi četnými technickými specifikacemi 3GPP. Když konstruktér protokolů čte ve specifikaci „pole INF“, okamžitě chápe, že odkazuje na tuto sekci užitečných dat proměnné délky specifickou pro daný typ zprávy. Toto konceptuální znovupoužití snižuje nejednoznačnost a urychluje vývoj a testování kompatibilních zařízení, od mobilních telefonů po síťovou infrastrukturu.

## Klíčové vlastnosti

- Pole proměnné délky sloužící jako kontejner pro užitečná data protokolové zprávy
- Obsah a struktura jsou definovány konkrétním protokolem a typem zprávy
- Typicky obsahuje sekvenci informačních prvků (IEs) s kódováním tag-délka-hodnota
- Umožňuje efektivní využití přenosové kapacity tím, že se vyhýbá výplni pevně dlouhých zpráv
- Poskytuje inherentní rozšiřitelnost pro přidávání nových parametrů v budoucích verzích protokolu
- Základní konstrukce používaná napříč více protokoly řídicí roviny 3GPP (např. RRC, NAS)

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [INF na 3GPP Explorer](https://3gpp-explorer.com/glossary/inf/)
