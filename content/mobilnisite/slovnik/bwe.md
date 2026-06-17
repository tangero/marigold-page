---
slug: "bwe"
url: "/mobilnisite/slovnik/bwe/"
type: "slovnik"
title: "BWE – BandWidth Extension"
date: 2025-01-01
abbr: "BWE"
fullName: "BandWidth Extension"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bwe/"
summary: "BandWidth Extension (BWE) je funkce 3GPP zavedená v Release 18 za účelem zlepšení kvality zvuku v hlasových a multimediálních službách rozšířením zvukového pásma mimo tradiční úzkopásmové limity. Umož"
---

BWE je funkce 3GPP Release 18, která zlepšuje kvalitu zvuku v hlasových a multimediálních službách rozšířením zvukového pásma mimo tradiční úzkopásmové limity.

## Popis

BandWidth Extension (BWE) je sofistikovaná technologie zpracování zvuku integrovaná do kodekového rámce 3GPP Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)), navržená k umělému rozšíření vnímaného zvukového pásma řečových signálů. Základní princip spočívá v analýze úzkopásmového nebo superširokopásmového zvukového vstupu (typicky do 8 kHz nebo 16 kHz) a generování vysokofrekvenčních složek (až do 20 kHz a výše), které původně přenášeny nebyly. Toho je dosaženo pomocí pokročilých algoritmů zpracování signálu, které modelují spektrální charakteristiky přirozené řeči, což přijímači umožňuje rekonstruovat plnopásmový zvukový signál, který subjektivně zní bohatěji a přirozeněji než původně přenášené pásmo.

Architektura BWE funguje v rámci flexibility pásma kodeku EVS. Působí jako postprocesní vylepšení na přijímací straně a spolupracuje se základním dekodérem. Mezi klíčové komponenty patří modul spektrální analýzy, který zkoumá přijímaný signál nižšího pásma, mechanismus odhadu parametrů, který predikuje chybějící vysokofrekvenční spektrální obálku a jemnou strukturu, a syntetizační banka filtrů, která generuje signál s rozšířeným pásmem. Proces je řízen pomocnou informací, která může být minimálně vložena do bitového toku pro navádění extenzního algoritmu, ačkoli velká část rozšíření je dosažena pomocí technik slepého odhadu, které nevyžadují žádnou nebo jen velmi nízkou režii dodatečné přenosové rychlosti.

Role BWE v síti je primárně na aplikační vrstvě v rámci řetězce mediálního zpracování hlasových a multimediálních služeb. Je implementováno v koncových uživatelských zařízeních (UE) a potenciálně v síťových prvcích, jako je Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) nebo aplikační servery pro konferenční scénáře. Technologie je obzvláště cenná v scénářích s omezenou šířkou pásma, kde by přenos plnopásmového zvuku byl neefektivní. Odesláním pouze základního signálu s nižší šířkou pásma a spoléháním se na BWE pro rekonstrukci vysokých frekvencí na straně přijímače mohou síťoví operátoři šetřit přenosovou kapacitu při zachování vysoké zvukové kvality. To z BWE činí klíčový prvek pro vysokokvalitní hlasové služby přes LTE (VoLTE), VoNR (Voice over New Radio) a další komunikace založené na IP Multimedia Subsystem (IMS).

Fungování BWE zahrnuje několik technických fází. Nejprve je přijímaný základní signál pásma (např. 0-8 kHz) transformován do frekvenční oblasti pomocí banky filtrů nebo transformace jako [MDCT](/mobilnisite/slovnik/mdct/) (Modified Discrete Cosine Transform). Jsou extrahovány spektrální rysy jako formanty, harmonické a spektrální sklon. Statistické modely nebo kodebooky, trénované na rozsáhlých databázích řeči, jsou pak použity k mapování těchto nízkopásmových rysů na pravděpodobné vysokopásmové spektrální parametry. Generované vysokopásmové spektrum je pečlivě tvarováno, aby se zabránilo artefaktům a zajistila přirozenost, často za použití zaplnění šumem pro nehlasové segmenty. Nakonec je rozšířené spektrum transformováno zpět do časové oblasti, což vede k plnopásmovému výstupnímu signálu. Celý proces je optimalizován pro nízkou výpočetní složitost, aby mohl efektivně běžet na mobilních zařízeních.

## K čemu slouží

BWE bylo vytvořeno, aby řešilo základní kompromis mezi zvukovou kvalitou a přenosovou šířkou pásma v mobilních komunikacích. Tradiční buněčné hlasové služby byly dlouho omezeny na úzkopásmový (300-3400 Hz) zvuk, který zní plechově a postrádá přirozenou bohatost konverzace tváří v tvář. Zatímco širokopásmový (50-7000 Hz) a superširokopásmový (50-14000 Hz) zvuk nabízel zlepšení, stále nedosahoval kvality plnopásmového (20-20000 Hz) zvuku a vyžadoval pro přenos podstatně větší šířku pásma. BWE to řeší tím, že umožňuje vnímat zážitek z plnopásmového zvuku bez úměrného nárůstu spotřeby síťových zdrojů.

Historický kontext vývoje BWE zahrnuje vývoj od přepojování okruhů k paketovým sítím VoLTE a VoNR, kde efektivita využití pásma zůstává klíčová navzdory rostoucí kapacitě. Předchozí přístupy buď přenášely celé spektrum (neefektivně), nebo jednoduše ořezávaly šířku pásma (ztráta kvality). BWE představuje chytřejší přístup, který využívá pokročilého zpracování zvukového signálu a psychoakustiky. Motivována byla uživatelskou poptávkou po vyšší kvalitě multimediálních zážitků na mobilních zařízeních, konkurenčním tlakem ze strany [OTT](/mobilnisite/slovnik/ott/) hlasových aplikací a potřebou síťových operátorů diferencovat své služby při efektivním řízení vzácných spektrálních zdrojů.

BWE konkrétně řeší omezení předchozích návrhů kodeků, které nabízely pevné režimy šířky pásma. Oddělením přenášené šířky pásma od vnímané výstupní šířky pásma poskytuje nebývalou flexibilitu. Síťoví operátoři mohou dynamicky upravovat základní přenášenou šířku pásma na základě síťových podmínek při zachování konzistentního vnímání vysoké kvality zvuku na uživatelském konci. To je obzvláště cenné v přetížených sítích nebo pro uživatele s omezenými datovými tarify. Dále BWE zlepšuje zpětnou kompatibilitu tím, že umožňuje starším zařízením podporujícím pouze užší pásma spolupracovat s novějšími zařízeními, přičemž stále těží z určitého zlepšení kvality díky zpracování rozšíření pásma.

## Klíčové vlastnosti

- Umělé generování vysokofrekvenčních zvukových složek (až do 20 kHz) ze vstupních signálů nižšího pásma
- Integrace s kodekovým rámcem 3GPP EVS dle specifikace TS 26.253
- Minimální režie přenosové rychlosti díky technikám slepého odhadu a parametrického kódování
- Zpětná kompatibilita s režimy dekódování užšího pásma
- Nízká výpočetní složitost vhodná pro implementaci v mobilních zařízeních
- Dynamická adaptace na síťové podmínky variací přenášené základní šířky pásma

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description

---

📖 **Anglický originál a plná specifikace:** [BWE na 3GPP Explorer](https://3gpp-explorer.com/glossary/bwe/)
