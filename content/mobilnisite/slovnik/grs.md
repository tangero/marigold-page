---
slug: "grs"
url: "/mobilnisite/slovnik/grs/"
type: "slovnik"
title: "GRS – Ground Radio Station"
date: 2025-01-01
abbr: "GRS"
fullName: "Ground Radio Station"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/grs/"
summary: "Pozemní radiostanice (GRS) je pozemní základnová stanice používaná v satelitních komunikačních sítích integrovaných se systémy 3GPP. Poskytuje pozemní rádiové rozhraní pro uživatelská zařízení, propoj"
---

GRS je pozemní základnová stanice v satelitní síti integrované podle 3GPP, která poskytuje pozemní rádiové rozhraní pro uživatelská zařízení a využívá satelity pro přenosový okruh (backhaul) k zajištění globálního pokrytí.

## Popis

Pozemní radiostanice (GRS) je v kontextu 3GPP pozemní síťový uzel, který tvoří klíčovou část architektury satelitní nebo neterestriální sítě (NTN). Funguje jako pozemní kotvící bod, který poskytuje rádiové rozhraní pro uživatelská zařízení (UE), podobně jako tradiční základnová stanice buňkové sítě (eNodeB/gNB), ale její přenosový okruh (backhaul) je realizován prostřednictvím satelitního spoje namísto pozemního vlákna nebo mikrovlnného spoje. GRS obsahuje rádiové transceivery, jednotky pro zpracování základního pásma a funkce pro vzájemné propojení potřebné k připojení 3GPP rádiové přístupové sítě k satelitní síti.

Z architektonického hlediska je GRS typicky nasazena na místě s volnou přímou viditelností na jeden nebo více satelitů. Komunikuje s uživatelskými zařízeními pomocí standardních 3GPP rádiových protokolů (např. LTE nebo NR) přes pozemní rádiové rozhraní. Na síťové straně GRS komunikuje se satelitem pomocí specifického satelitního rádiového rozhraní (např. založeného na DVB-S2X). GRS musí zvládat významné výzvy, jako jsou velmi dlouhé přenosové zpoždění (až stovky milisekund u geostacionárních satelitů), Dopplerovy posuny způsobené pohybem satelitu a časovou synchronizaci. Zahrnuje specifické protokoly a adaptace definované v 3GPP (např. v TS 36.305, 38.305), které maskují tyto satelitní charakteristiky před jádrem sítě, takže se GRS jeví pro 5GC nebo EPC jako standardní pozemní základnová stanice.

Klíčové komponenty v GRS zahrnují rádiovou jednotku (RU) pro pozemní rozhraní vzduchem, jednotku základního pásma ([BBU](/mobilnisite/slovnik/bbu/)) pro zpracování signálu, satelitní modem pro spojovací (feeder) okruh a funkci síťové adaptace. Tato adaptační funkce je zásadní; implementuje techniky kompenzace zpoždění, novým způsobem spravuje časový předstih pro satelitní spoj a může zajišťovat vyrovnávací paměť dat pro vyrovnání s dlouhou a proměnlivou latencí. Úlohou GRS je rozšířit pokrytí služeb 3GPP do odlehlých, námořních nebo leteckých oblastí, kde není pozemní infrastruktura dostupná nebo je neekonomická, a bezproblémově tak integrovat satelitní přístup do mobilního ekosystému.

## K čemu slouží

Pozemní radiostanice (GRS) byla zavedena, aby vyřešila základní problém poskytování všudypřítomného mobilního pokrytí založeného na 3GPP v oblastech mimo dosah pozemních sítí. Tradiční buňkové sítě jsou limitovány náklady a fyzickou obtížností nasazení vlákna a základnových stanic v oceánech, pouštích, polárních oblastech a při katastrofických scénářích, kdy je infrastruktura poškozena. GRS jako součást architektury neterestriální sítě (NTN) využívá globální pokrytí satelitních sítí k vyplnění těchto mezer v pokrytí.

Motivací pro standardizaci GRS v rámci 3GPP, zejména od Release 8 pro dřívější studie satelitní integrace a robustněji v pozdějších releasech pro 5G, bylo zajistit kontinuitu služeb a interoperabilitu. Bez standardizovaného konceptu pozemní stanice by byl satelitní přístup proprietární, neintegrovanou službou. GRS poskytuje definovaný síťový uzel, který umožňuje mobilním jádrovým sítím (EPC, 5GC) zacházet se satelitním pokrytím jako s rozšířením pozemní RAN, což umožňuje funkce jako mobilita mezi pozemními a satelitními buňkami a konzistentní autentizaci a účtování.

Historicky začaly rané release 3GPP (např. Rel-8) studovat satelitní komponenty, ale tlak zesílil s cílem 5G spojit vše všude. GRS řeší omezení předchozích ad-hoc satelitních telefonních systémů tím, že integruje satelitní přístup přímo do hlavního protokolového stacku 3GPP. To umožňuje standardním komerčním smartphonům, případně s drobnými úpravami, připojit se přes satelit prostřednictvím GRS, což otevírá nové případy užití pro IoT, nouzovou komunikaci a konektivitu za letu.

## Klíčové vlastnosti

- Poskytuje standardní 3GPP (LTE/NR) rádiové rozhraní pro uživatelská zařízení na zemi
- Spolupracuje se satelitními sítěmi prostřednictvím spojovacího (feeder) okruhu (např. pomocí DVB-S2X)
- Implementuje funkce síťové adaptace pro kompenzaci dlouhých přenosových zpoždění satelitního spoje
- Zvládá významnou korekci Dopplerova posunu způsobeného pohybem satelitu
- Jeví se jádrové síti 5GC nebo EPC jako standardní pozemní gNB nebo eNodeB
- Umožňuje kontinuitu služeb a mobilitu mezi pozemními a neterestriálními sítěmi

## Definující specifikace

- **TR 22.829** (Rel-17) — Enhancement for UAVs; Stage 1
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [GRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/grs/)
