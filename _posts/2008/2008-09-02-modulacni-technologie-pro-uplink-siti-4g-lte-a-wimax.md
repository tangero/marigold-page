---
ID: 2276
title: Modulační technologie pro uplink sítí 4G - OFDMA versus SC-FDMA
author: Patrick Zandl
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/modulacni-technologie-pro-uplink-siti-4g-lte-a-wimax
published: true
post_date: 2008-09-02 11:54:00
categories: [Mobilní sítě, LTE, 4G]
---
V další části povídání o vývoji situace v mobilních datech jsem se chtěl podívat na rozvoj WiMaxu a LTE, jenže jsem si s hrůzou povšiml, že o LTE jako technologii je na Marigoldovi jen málo. Takže musíme splatit dluh. Ještě před tím, než si nové 4G technologie (LTE, WiMax a UWB) porovnáme - to asi někdy příště - tak se mrkneme na rozdíly mezi způsobem modulace signálu. 
<!--more-->


Zatímco jak LTE (tedy Long Term Evolution pro UMTS), tak WiMax používají pro downlink <strong>OFDM</strong>, ortogonální frekvenčně dělený multiplex, pro uplink je u WiMaxu <strong>OFDMA</strong> (Ortogonální frekvenčně dělený vícenásobný přístup, Orthogonal Frequency Division Multiple Access),  zatímco pro LTE se standardizační skupina 3GPP rozhodla pro <strong>SC-FDMA</strong>, Single Carrier Frequency Division Multiple Access - frekvenčně dělený vícenásobný přístup na jedné nosné. 

Ačkoliv to vypadá, jako zásadní odlišnost, je třeba připomenout, že obojí spadá pod OFDM, tedy příbuznost obou přístupů je značná a pro návrháře čipů nejde o tak podstatnou změnu. Navíc označení SC-FDMA je částečně zavádějící, protože podobně jako u OFDMA je i zde využíváno více pod-nosných (sub-carrier). Jen tak na okraj, odpusťe pokusy s překlady, ono když si čtete český text s promíchanými velkými anglickými pasážemi, vypadá to víc otřesně, než když to jen slyšíte. 

<h2>OFDMA</h2>
OFDMA přenáší data využitím více úzkopásmových pod-nosných najednou, například 512, 1024 nebo ještě více v závislosti na použité/dostupné šířce pásma pro konkrétní kanál (tedy 5, 10, 15 či 20 MHz). Neboť je více bitů přenášeno současně,  je také přenosová rychlost na každé pod-nosné výrazně nižší, než výsledná rychlost dat. To je důležité z hlediska praktického použití v rádiovém prostředí, protože to vede k minimalizaci efektu vícecestného zpoždění způsobenému rozdílnými časy příchodu různě odražených signálů na základnovou stanici. 

Popíšeme si, jak to schematicky funguje, viz obrázek 1. 

<div style="text-align:center;"><img src="/assets/ofdma.png" alt="OFDMA.png" border="0" width="500" /></div>

Začneme vysílačem: přenášené bity jsou seskupeny a přiřazeny k přenosu na jednotlivých frekvencích (tzv. pod-nosných) - dojde k vytvoření (nebo též rozprostření do) pod-nosných. V tomto příkladu jsou 4 bity (představující modulaci 16QAM) použity k vytvoření takových pod-nosných. Teoreticky by se měl o každou sub-nosnou starat zvláštní vysílač, ale protože těch pod-nosných je opravdu hodně, není to zrovna praktické řešení. Místo toho nastupuje matematika: jelikož každá pod-nosná je vysílána na jiné frekvenci, můžeme vytvořit křivku, kde na ose X je frekvence a na ose Y je amplituda každé sub-nosné. Což je ten grafíček pod každým z nákresů. Následně je na křivku aplikována inverzní rychlá Fourierova transformace (IFFT), která převede frekvenční oblast do oblasti časové. Taková křivka pak má na ose X čas a přitom představuje ten samý signál, jaký by byl generován separátním přenosem každé pod-nosné. Moc hezká vychytávka! Pak už je přidána jen hlavička <strong>CP (cyclic prefix)</strong>, signál modulován, patřičně zesílen (podle dalších parametrů sítě) a odvysílán. 

Na straně přijímače (spodní část nákresu) je signál nejdříve demodulován a zesílen. Výsledný signál je pak přeměněn rychlou Fourierovou transformací (FFT) inverzně k předešle uvedenému postupu, čas opět nahradí frekvence. Tím dostáváme frekvenčně amplitudový diagram vytvořený původně na vysílači. Na středové frekvenci každé pod-nosné jsou pak detekční funkcí generovány bity, které zde byly původně zakódovány. Tím celý OFDMA proces vlastně končí. 

<h2>SC-FDMA</h2>
Přes své jméno frekvenčně dělený vícenásobný přístup na jedné nosné (SC-FDMA) také přenáší data vzduchem na více pod-nosných, pouze přidává do celého výše uvedeného procesu další kroky, viz obrázek 2: 

<div style="text-align:center;"><img src="/assets/sc-fdma.png" alt="SC-FDMA.png" border="0" width="500" /></div>

Místo toho, aby byly čtři bity použity k vytvoření signálu pro pod-nosné, jako je tomu u OFDMA, rozprostřou se informace přes všechny pod-nosné. To se udělá následovně: určitý počet bitů (například 4 při 16QAM modulaci) se seskupí dohromady. U OFDMA by tato skupina bitů prošla IDFT, v případě SC-FDMA je na ní aplikována rychlá Fourierova transformace (FFT). Výsledkem tohoto postupu je báze dat, která je použita pro vytvoření pod-nosných. Ty jsou už jako v případě OFDMA převedeny už pomocí IFFT z frekvencí na čas. Ne všechny pod-nosné jsou mobilkou použity a v diagramu jsou udávány jako nula. Tyto podnosné mohou a nemusí být použity jinými mobilkami. Ještě jsou přidány hlavičky <strong>CP (cyclic prefix)</strong>, které jsou vlastně hraičním pásmem mezi více bloky a zamezují rušení v rámci bloků při problémech s vícecestnými odrazy, kde jsou jednotlivé přijímané signály časově posunuty. Způsob aplikace CP by si zasloužil samostatný výklad, ale tu ho zanedbáváme. 

Na straně přijímače je signál demodulován, zesílen, odebrán je CP a výsledek prohnán rychlou Fourierovou transformací (FFT) tak, jako u OFDMA. Výsledný amplitudový diagram ovšem není analyzován přímo, aby z něj byla získána přenášená data, ale je na něj aplikována inverzní rychlý Fourierova transformace (IFFT). Výsledkem je signál orientovaný časově, ten je prohnán blokem detektoru, jenž z něj udělá přenášená data. Takto je použit pouze jeden detektor na jedné nosné, místo toho, aby byly detekovány bity na více pod-nosných. Odtud také ta zkratka.

Přiřazení konkurenčních uživatelů na pod-nosné
Výše uvedené schéma pro jednoduchost předpokládá jednu mobilku v síti. To ovšem v praxi není právě obvyklá konfigurace, většinou se setkáváme s více mobilkami. A tady přichází ono zesložitění, protože je třeba patřičně přiřadit konkurenční uživatele (=ti, kteří chtějí najednou odesílat data) na nosnou, tedy správně je rozházet do podnosných. 

V zásadě uvažujeme o dvou základních postupech přiřazení:
<ul>
<li>distribuovaný mód</li>
<li>lokalizovaný mód</li>
</ul>

V distribuovaném módu jsou přenosy jednotlivých konkurenčních uživatelů střídány po sobě, u lokalizovaného jsou přenosy jednoho uživatele za sebou, teprve pak následují přenosy dalšího uživatele. Jak to zhruba vypadá, vidíte na dalším obrázku (Obr. 3), kde jsou zachyceny tři terminály na dvanácti podnosných, přičemž každý uživatel požaduje 4 podnosné pro své přenosy:

<div style="text-align:center;"><img src="/assets/subcarier-mody.png" alt="subcarier-mody.png" border="0" width="506" height="144" /></div>

Zde zakreslený distribuovaný režim je označovaný jako <strong>Interleaved FDMA</strong>, tedy <strong>IFDMA</strong> - odstup mezi pod-nosnými užitými jednotlivými uživateli je konstantní. Lokalizovaný mód se označuje jako <strong>LFDMA</strong>. 

Proč si o tom povídáme? Protože způsob přiřazení konkurenčních uživatelů na pod-nosné hodně určuje výsledný PARP a také celkovou kapacitu uplink kanálu i kapacitu pro jednoho uživatele. Ačkoliv IFDMA poskytuje nižší PARP a tedy menší interference na uplinku, jeho problémem je pulse shaping. Výzkumy provedené v rámci standardizačního procesu ukazují, že v praxi se lépe osvědčí LFDMA s kanálově závislým plánováním (CDS - channel dependent scheduling), které nabídne větší kapacitu pro uživatele, než IFDMA. V každém případě je ale výsledek IFDMA i LFDMA lepší, než u OFDMA používaného WiMaxem. 

<h2>Rozdíly mezi oběma technologiemi</h2>

OFDM vezme skupinu vstupních bitů, z nich jsou vytvořeny pod-nosné a ty jsou zpracování IDFT tak, aby z nich vznikl časový signál. SC-FDMA oproti tomu nejprve provede FFT na skupině vstupních bitů, aby je rozprostřela mezi všechny pod-nosné a pak použije výsledek pomocí IDFT k vytvoření časového signálu. Kvůli této odlišnosti se někdy také SC-FDMA označuje jako <strong>DFT-spread</strong> nebo <strong>DFT-precoded OFDMA</strong>, tedy rozprostření pomocí diskrétní Fourierovi transformace. 

Vidíme zřetelně, že toto rozprostírání přidává další nároky jak na straně vysílače, tak přijímače. Otázka je, proč toto řešení bylo zvoleno v LTE. Důvod je jednoduchý: snížení <strong>PAPR</strong>, tedy poměru špičkového a průměrného výkonu: <strong>Peak to Average Power Ratio</strong>. Tento poměr je u samotného OFDMA příliš vysoký, což znamená nejenom vyšší nároky na baterie telefonu, ale také riziko zarušení vlastní sítě zbytečně vysokým vysílacím výkonem mobilky. Právě použitím SC-FDMA se poměr PAPR významně snižuje, čímž dochází jak k úspoře baterií, tak k vyšší přenosové rychlosti na uplinku. 

Poznámka pro lidi, které mate občasná záměna diskrétní fourierovy transformace DFT a rychlé fourierovy transformace FFT - to druhé je praktická implementace toho prvního. 



