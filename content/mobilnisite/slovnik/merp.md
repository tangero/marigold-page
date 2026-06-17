---
slug: "merp"
url: "/mobilnisite/slovnik/merp/"
type: "slovnik"
title: "MERP – Mean Effective Radiated Power"
date: 2025-01-01
abbr: "MERP"
fullName: "Mean Effective Radiated Power"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/merp/"
summary: "Mean Effective Radiated Power (MERP, střední efektivní vyzařovaný výkon) je regulační a výkonnostní metrika představující průměrný výkon vysílaný z rádiové antény, která bere v úvahu jak výstupní výko"
---

MERP je regulační metrika pro průměrný výkon vyzařovaný z antény, která zohledňuje jak výstupní výkon vysílače, tak zisk antény.

## Popis

Mean Effective Radiated Power (MERP, střední efektivní vyzařovaný výkon) je standardizovaná míra vysokofrekvenčního výkonu vyzařovaného vysílací stanicí, například uživatelským zařízením (UE) v mobilní síti. Představuje průměrný výkon dodávaný do antény násobený ziskem antény vůči izotropnímu zářiči (dBi) v určitém směru. Matematicky, pro daný směr, MERP (v dBm) = Výstupní výkon vysílače (dBm) + Zisk antény (dBi) - Ztráty ve vývodovém vedení. Aspekt 'Mean' (střední) značí, že se jedná o průměr přes výkyvy výkonu modulačního schématu (např. průměrování obálky výkonu signálu QPSK nebo [OFDM](/mobilnisite/slovnik/ofdm/)). 'Effective' (efektivní) označuje, že metrika zohledňuje schopnost antény soustředit energii, což z ní činí přesnější reprezentaci síly signálu ve vzdáleném poli než samotný výkon vysílače.

Stanovení MERP zahrnuje jak výpočty ve fázi návrhu, tak regulační testování. Pro UE je maximální MERP klíčovým parametrem definovaným v jeho specifikacích rádiové shody. Při testování je UE umístěno v anechoické komoře nebo kalibrovaném testovacím uspořádání. Pomocí referenční měřicí antény a výkonového měřiče nebo spektrálního analyzátoru se změří ekvivalentní izotropně vyzařovaný výkon ([EIRP](/mobilnisite/slovnik/eirp/)). Jelikož je MERP pro praktické účely v 3GPP v podstatě synonymem pro EIRP, je toto změřený vyzařovaný výkon, který je ověřován vůči regulačním limitům (např. stanoveným [FCC](/mobilnisite/slovnik/fcc/) nebo [ETSI](/mobilnisite/slovnik/etsi/)) a požadavkům 3GPP na maximální výkon. Měření zohledňuje činnost UE při jeho maximálním nastavení řízení výkonu pro podporovanou výkonovou třídu a kmitočtové pásmo.

Jeho role v síti je mnohostranná. Pro provozovatele sítí a regulátory je MERP klíčový pro zajištění souladu s pravidly licencování spektra, která definují maximální povolené úrovně výkonu za účelem kontroly interference mezi různými sítěmi a službami. Pro plánování rádiové sítě znalost typické hodnoty MERP UE pomáhá inženýrům přesně modelovat výkonovou bilanci uplinku. Ta určuje plochu pokrytí buňky, zejména na uplinku, který je často limitujícím článkem. Citlivost přijímače základnové stanice je vyvažována vůči MERP UE, aby byla zajištěna spolehlivá komunikace na okraji buňky. Dále se MERP používá při hodnocení expozice z hlediska vysokofrekvenční (RF) bezpečnosti, protože přímo souvisí s hustotou výkonu, které je uživatel ze zařízení vystaven.

## K čemu slouží

MERP byl standardizován, aby poskytl konzistentní, měřitelnou a pro regulaci relevantní definici vysílaného výkonu rádiového zařízení. Před takovou standardizací byly termíny jako 'výkon vysílače' nejednoznačné, protože ignorovaly významný vliv antény. Dvě zařízení se stejným výstupním výkonem vysílače, ale s různými anténami, mohou mít zcela odlišný dopad na síť a interferenční prostředí. MERP to řeší definicí vyzařovaného výkonu, což je skutečná veličina, která se šíří prostorem a ovlivňuje další přijímače.

Jeho vytvoření bylo motivováno potřebou spravedlivého sdílení spektra, bezpečnostními předpisy a přesného návrhu systémů. Regulační orgány vyžadují limity vyzařovaného výkonu, aby zabránily nadměrnému rušení. Výrobci zařízení potřebují jasný cíl pro návrh a certifikaci. Plánovači sítí vyžadují přesný parametr pro simulaci pokrytí. MERP uspokojuje všechny tyto potřeby tím, že je jedinou komplexní metrikou, která zahrnuje kombinovaný účinek vysílače a antény. Je obzvláště důležitý pro mobilní zařízení, kde se výkon antény může výrazně lišit v závislosti na návrhu, formátu a způsobu držení zařízení (ztráty vlivem těla). Standardizace jeho definice a metody měření ve specifikacích 3GPP zajišťuje globální interoperabilitu a konzistentní testování shody.

## Klíčové vlastnosti

- Představuje průměrný vyzařovaný výkon včetně zisku antény
- Klíčový parametr pro regulační shodu a testování shody
- Základní vstup pro výpočty výkonové bilance uplinku
- Měřený v anechoických komorách pomocí standardizovaných metod
- Definovaný pro každou výkonovou třídu UE a provozní kmitočtové pásmo
- Používaný při hodnocení RF expozice a bezpečnosti (SAR)

## Související pojmy

- [EIRP – Effective Isotropic Radiated Power](/mobilnisite/slovnik/eirp/)

## Definující specifikace

- **TR 25.914** (Rel-19) — 3G UE Radio Performance Test Methods

---

📖 **Anglický originál a plná specifikace:** [MERP na 3GPP Explorer](https://3gpp-explorer.com/glossary/merp/)
