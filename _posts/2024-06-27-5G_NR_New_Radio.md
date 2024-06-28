---
title: New Radio (NR) v Release 15&#8282; Revoluční základ pro 5G sítě  
post_excerpt: "3GPP Release 15, finalizovaný v roce 2018, představuje milník v evoluci mobilních sítí. Jádrem tohoto vydání je New Radio (NR), zcela nové rádiové rozhraní navržené speciálně pro 5G sítě. NR přináší zásadní změny v architektuře a funkčnosti mobilních sítí, což umožňuje dosáhnout tolik žádaný výkon, flexibilitu a škálovatelnost."
layout: post
categories: [Mobilní sítě, 5G]
hide: true 
---

3GPP Release 15, finalizovaný v roce 2018, představuje milník v evoluci mobilních sítí. Jádrem tohoto vydání je New Radio (NR), zcela nové rádiové rozhraní navržené speciálně pro 5G sítě. NR přináší zásadní změny v architektuře a funkčnosti mobilních sítí, což umožňuje dosáhnout tolik žádaný výkon, flexibilitu a škálovatelnost.

New Radio v Release 15 představuje fundamentální přestavbu mobilních sítí. Zatímco LTE bylo evolucí 3G systémů, NR je revolucí, která od základů mění způsob, jakým navrhujeme a implementujeme mobilní sítě. S jeho flexibilitou, škálovatelností a výkonem NR nejen splňuje současné požadavky na mobilní komunikaci, ale také pokládá robustní základ pro budoucí inovace v oblasti 5G a beyond 5G systémů.

## Klíčové aspekty NR

Podívejme se v bodech na to, co je v NR nové a důležité:

1.  **Flexibilní struktura rámce** -  NR zavádí flexibilní strukturu rámce s různými možnostmi délky slotu a mezislotového intervalu. Na rozdíl od fixní struktury LTE (10ms rámec, 1ms subrámec), NR umožňuje dynamickou adaptaci na různé scénáře použití. Je to jako konečně dodělat do automobilu převodovku, aby bylo možné měnit převodový poměr podle jízdních podmínek.
2.  **Škálovatelné číslování nosných** -  NR podporuje širokou škálu šířek pásma (od 5 MHz až po 400 MHz) s flexibilním číslováním nosných. To kontrastuje s rigidním přístupem LTE, kde šířka pásma byla omezena na maximálně 20 MHz. Tím se Nové Rádio stává modulární stavebnici, kde lze snadno přidávat nebo odebírat bloky podle potřeby.
3.  **Masivní MIMO a formování paprsku (beamforming)** NR plně využívá potenciál masivního MIMO a pokročilého formování paprsku. Zatímco LTE již zavedlo základy MIMO, NR posouvá tuto technologii na zcela novou úroveň. Analogií může být přechod od jednoduchého zahradního postřikovače (LTE) k sofistikovanému systému přesného zavlažování (NR), který cíleně distribuuje vodu tam, kde je potřeba.
4.  **Nové modulační schéma** - NR zavádí **256QAM** pro downlink i uplink, oproti LTE, které používalo 64QAM pro uplink. Je to opravdu znatelný rozdíl v efektivitě umožňující přenos většího množství dat ve stejném spektrálním prostoru.
5.  Podpora **mmWave frekvencí** Jednou z nejvýznamnějších inovací NR je podpora mmWave frekvencí (24 GHz a výše). To otevírá zcela nové možnosti pro ultra-vysokorychlostní přenosy dat, ale zároveň přináší nové výzvy v oblasti pokrytí.
6.  **Nativní podpora nízké latence** - NR je navržen s ohledem na ultra-nízkou latenci (URLLC - Ultra-Reliable Low-Latency Communication). To zahrnuje kratší intervaly přenosu (TTI) a možnost přednostního zpracování kritických dat.
7.  **Network Slicing** - Ačkoli není výhradně součástí rádiového rozhraní, NR je navržen s ohledem na network slicing. To umožňuje vytvoření virtuálních sítí s různými charakteristikami na stejné fyzické infrastruktuře. Pro každý typ služby používané v mobilní síti a tedy pro uživatele používajícího momentálně tuto službu lze zvolit jen ty části sítě, které jsou pro obsluhu takové služby bezpodmínečně nutné - a tím urychlit provoz i snížit nároky na síť.
8.  **Nová architektura sítě** NR přináší možnost samostatného (SA Standalone) nebo nesamostatného (NSA Non Standalone) nasazení. NSA využívá existující LTE infrastrukturu pro řídící rovinu, zatímco SA představuje čistě 5G řešení. Toto lze přirovnat k hybridnímu automobilu (NSA) versus plně elektrickému vozidlu (SA).

Když jsme u těch nových frekvencí mmWave, jaká je představa, kde a jaké frekvence se budou používat?

![využití frekvencí v rámci NR](/assets/5g-nr-frekvence.png)

    
Hlavní uživatelské rozdíly mezi  5G NR a LTE:

1.  Spektrální efektivita: NR dosahuje až 30% zlepšení spektrální efektivity oproti LTE.
2.  Latence: NR cílí na latenci pod 1 ms, oproti ~10 ms u LTE. 
3.  Připojená zařízení: NR podporuje až 1 milion zařízení na km², oproti ~100,000 u LTE.
4.  Rychlost přenosu dat: NR umožňuje teoretické rychlosti až 20 Gbps, zatímco LTE-Advanced dosahuje maximálně 1 Gbps.
    
Pro jaké aplikace se 5G NR hodí?

![Vymezení aplikací pro 5G NR](/assets/5G-NR_applications.png)

Zde je tabulka porovnávající klíčové aspekty New Radio (NR) z Release 15 s předchozími přístupy v LTE:

| Aspekt | LTE | NR (Release 15) |
|--------|-----|-----------------|
| Struktura rámce | Fixní: 10ms rámec, 1ms subrámec | Flexibilní: různé délky slotu (0.125ms - 1ms) |
| Šířka pásma | Až 20 MHz (do 100 MHz s CA) | 5 MHz - 400 MHz |
| Číslování nosných | Fixní rozestupy | Škálovatelné rozestupy (15 kHz, 30 kHz, 60 kHz, 120 kHz, 240 kHz) |
| Frekvenční pásma | Primárně pod 6 GHz | Pod 6 GHz a mmWave (až do 52.6 GHz) |
| MIMO | Do 8x8 MIMO | Masivní MIMO (až 256 antén) |
| Modulace (DL/UL) | 256QAM/64QAM | 256QAM/256QAM |
| Latence | ~10 ms | Cílí na <1 ms (URLLC) |
| Formování paprsku | Základní | Pokročilé 3D beamforming |
| Hustota připojení | ~100,000 zařízení/km² | Až 1 milion zařízení/km² |
| Maximální rychlost dat | 1 Gbps (LTE-Advanced) | Teoreticky až 20 Gbps |
| Duplexní režimy | FDD, TDD | FDD, TDD, flexibilní TDD |
| Network Slicing | Není nativně podporováno | Nativní podpora |
| Architektura | Pevně daná | Flexibilní (NSA, SA) |
| Kódování | Turbo kódy | LDPC (data), Polar kódy (kontrolní informace) |
| Energetická účinnost | Standardní | Vylepšená (nové režimy spánku) |
| Podpora IoT | LTE-M, NB-IoT | Vylepšená podpora mMTC |
| Spektrální efektivita | Baseline | Až o 30% vyšší |
| Podpora Vehicle-to-Everything (V2X) | Základní (LTE-V) | Pokročilá (NR V2X) |
| Škálovatelnost pro různé use cases | Omezená | Vysoká (eMBB, URLLC, mMTC) |

NR (New Radio) se v následujících vydáních 3GPP po Release 15 dále vyvíjí a zdokonaluje. Podívejme se ještě pro jistotu na směry, jimiž se rozvoj NR vydává až do Release 18 schválené v roce 2024:

### Release 16 (2020):

1. NR-Unlicensed (NR-U): Rozšíření NR do nelicencovaného spektra.
2. Vylepšení URLLC: Další snížení latence a zvýšení spolehlivosti.
3. Vehicle-to-Everything (V2X): Pokročilá podpora pro automobilové aplikace.
4. Integrated Access and Backhaul (IAB): Umožňuje 5G základnovým stanicím fungovat jako relay pro backhaul.
5. Positioning: Vylepšené možnosti určování polohy v NR sítích.
6. MIMO vylepšení: Další zdokonalení multi-user MIMO.
7. 2-step RACH: Zjednodušený přístupový proces pro snížení latence.

### Release 17 (2022):

1. NR-Light (RedCap): Podpora zařízení se sníženými schopnostmi pro IoT aplikace.
2. NR nad 52.6 GHz: Rozšíření podpory do vyšších frekvenčních pásem.
3. Non-Terrestrial Networks (NTN): Podpora pro satelitní a vzdušné platformy.
4. Multi-SIM: Vylepšená podpora pro zařízení s více SIM kartami.
5. Sidelink vylepšení: Rozšířené možnosti pro přímou komunikaci mezi zařízeními.
6. Vylepšení pro průmyslový IoT a URLLC.
7. Multicast a broadcast služby: Efektivnější distribuční mechanismy.
8. AI/ML integrace do rádiového rozhraní.

### Release 18 (2024) - První vydání 5G-Advanced:

1. Další rozšíření AI/ML v RAN: Včetně AI/ML pro beamforming, MIMO a další RF technologie.
2. Rozšířené imersivní komunikace: Podpora pro XR (Extended Reality) aplikace.
3. Vylepšení RedCap: Další optimalizace pro IoT a wearable zařízení.
4. Pokročilé MIMO techniky: Včetně "full-duplex" MIMO.
5. Vylepšení pro energetickou účinnost sítě a zařízení.
6. Další rozšíření spektra: Včetně pásem nad 71 GHz.
7. Vylepšení pro poziční služby: Centimetrová přesnost pro indoor i outdoor prostředí.
8. RAN slicing vylepšení: Pokročilejší možnosti pro network slicing na úrovni RAN.
9. Vylepšení pro mobilní širokopásmové připojení: Zaměření na zvýšení kapacity a pokrytí.
10. Další integrace nezemských sítí (NTN).

Tyto technologie a vylepšení nejen dále zdokonalují základní schopnosti NR definované v Release 15, ale také otevírají nové možnosti pro aplikace a use cases. Důraz je kladen na zvýšení flexibility, efektivity, spolehlivosti a výkonu NR, stejně jako na podporu nových typů služeb a aplikací.

Jsou také technologie, které se v rámci návrhu NR zvažovaly a nakonec zavrhly. Například OFDMA mohla nahradit či doplnit jako přístupová metoda  NOMA (Non-Orthogonal Multiple Access). Ta nabízela v řadě scénářů lepší efektivitu využití rádiového spektra, než OFDMA, ale také vyžadovala dražší hardware a především, není zpětně kompatibilní s LTE, což byl jeden z hlavních požadavků. Kromě toho NOMA není příliš přesvědčivá v podmínkách vysokého poměru signálu k šumu. A nakonec tu byly patentové problémy. A tak se prosadil pohled, že zejména další rozvoj MIMO a beamformingu výhody NOMA převáží v rozvoji OFDMA. Což ale není definitivní konec, aspekty NOMA jsou dále zkoumány a mohou se ve standardu objevit později, podobně jako například Filtrovaná OFDM (f-OFDM) nebo Full Duplex Radio.

A ještě se podívejme na jednu věc. Jaký je vztah mezi NR a RAN, například C-RAN nebo Open RAN?  NR a C-RAN jsou dvě různé, ale vzájemně se doplňující technologie v ekosystému 5G. NR definuje "jak" komunikovat na rádiové úrovni, zatímco C-RAN poskytuje flexibilní a škálovatelnou architekturu pro "kde" a "jak efektivně" implementovat zpracování signálu. Jejich kombinace umožňuje plné využití potenciálu 5G sítí, poskytuje flexibilitu, výkon a efektivitu potřebnou pro podporu širokého spektra 5G use cases a služeb.

A to je ze základů New Radio pro 5G zatím všechno 😇

> Pokračujte dále na [Seriál Mobilní sítě](/mobilnisite/)