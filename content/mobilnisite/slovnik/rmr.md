---
slug: "rmr"
url: "/mobilnisite/slovnik/rmr/"
type: "slovnik"
title: "RMR – Railway Mobile Radio"
date: 2025-01-01
abbr: "RMR"
fullName: "Railway Mobile Radio"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rmr/"
summary: "Pracovní položka a soubor funkcí 3GPP standardizující mobilní připojení pro železniční provoz. Definuje vylepšené síťové architektury, požadavky na výkon a schopnosti zařízení pro podporu scénářů s vy"
---

RMR je soubor funkcí 3GPP, který standardizuje mobilní připojení pro železniční provoz definováním vylepšených architektur a požadavků pro podporu spolehlivé komunikace vysokorychlostních vlaků a kritických služeb.

## Popis

Railway Mobile Radio (RMR) je komplexní standardizační iniciativa v rámci 3GPP, zahájená ve vydání Release 17, která řeší specifické výzvy poskytování komunikačních služeb založených na mobilních sítích v železničním prostředí. Zahrnuje soubor specifikací definujících vylepšené síťové architektury, požadavky na výkon a funkce zařízení přizpůsobené pro vysokorychlostní vlaky, často přesahující 500 km/h. Práce pokrývá jak rádiový přístupový síť (RAN), tak jádro sítě, se zaměřením na zajištění plynulé mobility, spolehlivého výkonu rádiového spoje a podpory pro kritické železniční služby spolu s širokopásmovým přístupem pro cestující.

Z architektonického hlediska RMR ovlivňuje několik oblastí. Pro RAN specifikace jako TS 38.104 a TS 38.141 definují vylepšené požadavky na základnové stanice (gNB), včetně specifických referenčních měřicích kanálů a testů výkonu pro vysokorychlostní scénáře. TS 37.829 se zaměřuje na aspekty nasazení v železničním prostředí, analyzuje scénáře a definuje potenciální řešení pro zahušťování sítě podél tratí a pokročilé anténní systémy pro zvládnutí vysokého Dopplerova jevu a rychlých předávání spojení. Pro UE (palubní modem nebo zařízení cestujícího) specifikace TS 38.852 a TS 38.853 stanovují požadavky a testy shody pro železniční mobilitu, aby zařízení udržela konektivitu v extrémních podmínkách vlaku, jako je útlum pronikání kovovými skříněmi vozů a trvale vysoká rychlost.

Jak to funguje, zahrnuje vylepšení napříč více vrstvami. Síť musí podporovat efektivní mechanismy předávání spojení pro zvládnutí předvídatelného, lineárního pohybu vlaků podél koridoru. To může zahrnovat koordinaci mezi gNB a potenciální využití specifických stavů mobility. Správa rádiových zdrojů je optimalizována pro šíření dominované přímou viditelností a potřebu konzistentního pokrytí podél trati. Dále práce na RMR studuje potenciál síťového řezání pro izolaci kritických provozních železničních komunikací (např. pro signalizaci nebo palubní systémy) od veřejného provozu cestujících, což zajišťuje garantovanou kvalitu služby. Požadavky na výkon definované v těchto specifikacích zajišťují, že systém 5G může poskytnout potřebnou propustnost, latenci a dostupnost jak pro provozní technologie ([OT](/mobilnisite/slovnik/ot/)), tak pro informační technologie ([IT](/mobilnisite/slovnik/it/)) aplikace na pohybujících se vlacích.

## K čemu slouží

Vytvoření pracovní položky Railway Mobile Radio ve vydání 3GPP Release 17 bylo motivováno potřebou globálního železničního průmyslu modernizovat své komunikační systémy. Tradiční vyhrazené mobilní rádiové systémy pro železnice (jako [GSM-R](/mobilnisite/slovnik/gsm-r/)) zastarávají, mají omezenou šířku pásma a jsou nákladné na údržbu. Průmysl usiloval o využití úspor z rozsahu, kontinuálního vývoje a vysokého výkonu veřejné mobilní technologie 3GPP (4G LTE a 5G NR) pro podporu jak kritických provozních služeb (řízení vlaků, video dohled, komunikace posádky), tak infotainmentu pro cestující.

RMR řeší významná technická omezení použití standardních mobilních sítí pro vysokorychlostní železnici. Standardní nasazení jsou optimalizována pro pěší a běžnou vozidlovou rychlost, nikoli pro vlaky pohybující se rychlostí přes 500 km/h, které způsobují extrémní Dopplerův jev, velmi krátkou dobu setrvání v buňce a náročné scénáře předávání spojení. Předchozí přístupy se buď spoléhaly na speciální, izolované sítě, nebo vykazovaly špatný výkon na veřejných sítích. RMR standardizuje vylepšení potřebná k tomu, aby se technologie 3GPP stala vhodnou pro toto náročné prostředí. Řeší problém interoperability, umožňuje železničním operátorům nakupovat standardizované síťové vybavení a palubní zařízení od více dodavatelů a zajišťuje, že výkon a spolehlivost potřebné pro bezpečnostně relevantní a podnikově kritické aplikace mohou být splněny pomocí jednotné, budoucím potřebám odolné mobilní platformy.

## Klíčové vlastnosti

- Standardizované požadavky na výkon pro scénáře s velmi vysokou rychlostí (>500 km/h)
- Vylepšené procedury mobility a předávání spojení pro lineární, předvídatelný pohyb
- Specifické testy shody UE pro železniční prostředí (TS 38.853)
- Studie modelů nasazení a síťových architektur pro železniční koridory
- Podpora koexistence kritických provozních a veřejných služeb pro cestující
- Řeší výzvy jako Dopplerův jev, útlum pronikání a rychlý převýběr buňky

## Definující specifikace

- **TR 37.829** (Rel-18) — Technical Report
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TR 38.852** (Rel-17) — 1900MHz NR band for European Rail Mobile Radio
- **TR 38.853** (Rel-17) — 900MHz NR Band for European Rail Mobile Radio

---

📖 **Anglický originál a plná specifikace:** [RMR na 3GPP Explorer](https://3gpp-explorer.com/glossary/rmr/)
