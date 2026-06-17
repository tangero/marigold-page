---
slug: "adpcm"
url: "/mobilnisite/slovnik/adpcm/"
type: "slovnik"
title: "ADPCM – Adaptive Differential Pulse Coded Modulation"
date: 2025-01-01
abbr: "ADPCM"
fullName: "Adaptive Differential Pulse Coded Modulation"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/adpcm/"
summary: "ADPCM je řečový kódovací algoritmus používaný v sítích 3GPP pro efektivní přenos hlasu. Komprimuje hlasové signály kódováním rozdílů mezi po sobě jdoucími vzorky namísto absolutních hodnot a adaptivně"
---

ADPCM je řečový kódovací algoritmus používaný v sítích 3GPP, který komprimuje hlas tím, že kóduje rozdíly mezi vzorky a adaptivně mění kvantizaci, čímž poskytuje dobrou kvalitu při nižších přenosových rychlostech.

## Popis

Adaptive Differential Pulse Coded Modulation (ADPCM, adaptivní diferenciální pulzně kódová modulace) je pokročilá řečová kódovací technika standardizovaná ve specifikacích 3GPP pro hlasové služby. Na rozdíl od tradiční PCM, která kóduje každý vzorek nezávisle, ADPCM používá diferenciální kódování, při kterém se přenáší pouze rozdíl mezi po sobě jdoucími vzorky. Tento základní přístup výrazně snižuje potřebnou přenosovou rychlost při zachování kvality řeči. 'Adaptivní' složka odkazuje na schopnost algoritmu dynamicky upravovat velikost kvantizačního kroku na základě charakteristik vstupního signálu, což umožňuje efektivnější kódování během období rychlých změn signálu a jemnější rozlišení během stabilních období.

V jádru ADPCM funguje prostřednictvím prediktivní kódovací struktury skládající se z adaptivního prediktoru a adaptivního kvantizéru. Prediktor odhaduje hodnotu dalšího vzorku na základě předchozích vzorků a vytváří predikovaný signál. Rozdíl mezi skutečným vstupním signálem a touto predikovanou hodnotou (chyba predikce) je následně kvantován pomocí adaptivního kvantizéru, jehož velikost kroku se přizpůsobuje podle rozptylu signálu. Tento kvantovaný rozdíl je zakódován pro přenos. V dekodéru stejný prediktor a adaptivní kvantizér rekonstruují původní signál z přenesených rozdílů, přičemž je zachována synchronizace mezi adaptačními algoritmy kodéru a dekodéru.

Implementace ADPCM v 3GPP specifikuje několik variant s různými přenosovými rychlostmi, nejvýznamněji ADPCM s 32 kbit/s definované v 3GPP TS 26.969. Tato implementace vychází ze standardu [ITU-T](/mobilnisite/slovnik/itu-t/) G.726, ale obsahuje specifické úpravy pro prostředí mobilních sítí. Algoritmus zpracovává řečové signály vzorkované na 8 kHz s 16bitovým rozlišením a komprimuje je na 4 bity na vzorek (32 kbit/s). Mezi klíčové komponenty patří adaptivní kvantizér se 16 možnými výstupními úrovněmi, adaptivní prediktor používající konfiguraci pól-nula a adaptační logika, která řídí úpravy velikosti kroku na základě velikosti nedávných kvantovaných rozdílů.

V rámci sítí 3GPP slouží ADPCM jako mezilehlý kodec mezi tradiční PCM s 64 kbit/s a pokročilejšími kodeky jako je [AMR](/mobilnisite/slovnik/amr/). Nachází uplatnění v různých scénářích včetně operací překódování, okruhově spínaných hlasových služeb a některých rozhraní legacy systémů. Architektura algoritmu zahrnuje detektory tónu a přechodu pro zpracování neřečových signálů, synchronizační mechanismy zabraňující rozcházení mezi kodérem a dekodérem a schopnosti generování komfortního šumu pro období ticha. Přestože byl v moderních sítích z velké části nahrazen efektivnějšími kodeky, ADPCM zůstává relevantní pro interoperabilitu s legacy systémy a specifické servisní scénáře, kde je jeho rovnováha mezi kvalitou a složitostí výhodná.

## K čemu slouží

ADPCM byl vyvinut k řešení základní výzvy efektivity využití šířky pásma v hlasové komunikaci. Tradiční pulzně kódová modulace (PCM) s 64 kbit/s poskytovala vynikající kvalitu hlasu, ale spotřebovávala značné síťové zdroje, což bylo obzvláště problematické v raných digitálních mobilních sítích s omezenou kapacitou. Telekomunikační průmysl potřeboval metodu pro snížení přenosové rychlosti hlasových signálů při zachování přijatelné kvality, což by umožnilo více simultánních hovorů ve stejném pásmu a snížilo náklady na přenos.

Před ADPCM nabízely jednoduché kompresní techniky jako logaritmická kompandace (μ-zákon/A-zákon PCM) pouze skromná zlepšení. Diferenciální PCM (DPCM) poskytovala lepší kompresi, ale trpěla degradací kvality během rychlých změn signálu. ADPCM tyto limity vyřešil zavedením adaptivní kvantizace, která se dynamicky přizpůsobuje charakteristikám signálu. To umožnilo kodeku přesněji sledovat řečové signály během přechodů při použití hrubší kvantizace během stabilních období, čímž dosáhl významného snížení přenosové rychlosti (z 64 kbit/s na 32 kbit/s nebo méně) s minimálním dopadem na kvalitu.

V rámci standardizace 3GPP sloužil ADPCM jako důležitá přechodová technologie mezi kodeky první generace digitálního hlasu a sofistikovanějšími algoritmy jako je [AMR](/mobilnisite/slovnik/amr/). Poskytoval praktické řešení pro síťové operátory migrující z legacy systémů a zároveň nabízel lepší spektrální účinnost než PCM. Tato technologie také umožnila efektivnější využití přenosových linek v páteřní síti a podporovala interoperabilitu mezi různými síťovými prvky, které mohly používat různé standardy řečového kódování. Ačkoli byl nakonec překonán pokročilejšími kodeky nabízejícími lepší kompresi při nižších přenosových rychlostech, ADPCM sehrál klíčovou roli ve vývoji digitálních hlasových služeb v mobilních sítích.

## Klíčové vlastnosti

- Diferenciální kódování snižující přenosovou rychlost přenosem rozdílů mezi vzorky
- Adaptivní kvantizace s dynamickou úpravou velikosti kroku na základě rozptylu signálu
- Provoz s rychlostí 32 kbit/s poskytující 2:1 kompresi oproti standardní PCM s 64 kbit/s
- Adaptivní prediktor typu pól-nula pro přesné odhadování signálu
- Detekce tónu a přechodu pro zpracování neřečových signálů
- Synchronizační mechanismy zabraňující neshodě mezi kodérem a dekodérem

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 26.969** (Rel-19) — eCall In-band Modem Performance Characterization
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 29.007** (Rel-19) — PLMN-PSTN/ISDN Interworking Requirements
- **TS 43.050** (Rel-19) — GSM Transmission Planning for Speech Services
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [ADPCM na 3GPP Explorer](https://3gpp-explorer.com/glossary/adpcm/)
