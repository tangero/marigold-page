---
slug: "sb-adpcm"
url: "/mobilnisite/slovnik/sb-adpcm/"
type: "slovnik"
title: "SB-ADPCM – Sub-Band Adaptive Differential Pulse-Code Modulation"
date: 2025-01-01
abbr: "SB-ADPCM"
fullName: "Sub-Band Adaptive Differential Pulse-Code Modulation"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sb-adpcm/"
summary: "Audio kodekový algoritmus standardizovaný organizací 3GPP pro kompresi hlasových a audio signálů. Kombinuje subpásmové kódování s ADPCM technikami, čímž dosahuje efektivního využití šířky pásma při za"
---

SB-ADPCM je audio kodekový algoritmus standardizovaný organizací 3GPP, který kombinuje subpásmové kódování s ADPCM technikami za účelem efektivní komprese hlasových a audio signálů pro telekomunikační služby.

## Popis

Sub-Band Adaptive Differential [PCM](/mobilnisite/slovnik/pcm/) (SB-ADPCM) je hybridní algoritmus pro kódování audia, který spojuje dvě základní techniky zpracování signálu: subpásmové kódování a adaptivní diferenciální pulzně kódovou modulaci ([ADPCM](/mobilnisite/slovnik/adpcm/)). Kodek funguje tak, že nejprve rozdělí vstupní audio signál (typicky vzorkovaný na 8 kHz nebo 16 kHz) na více frekvenčních subpásem pomocí banky filtrů, například kvadraturního zrcadlového filtru ([QMF](/mobilnisite/slovnik/qmf/)). Každé subpásmo je poté nezávisle zakódováno pomocí ADPCM kodéru. Samotná ADPCM funguje na principu predikce následující hodnoty vzorku na základě předchozích vzorků a následného kódování pouze rozdílu (chyby predikce) mezi skutečnou a predikovanou hodnotou. Tento rozdíl je kvantován pomocí adaptivního kvantizéru, jehož krok se dynamicky přizpůsobuje charakteristikám signálu, aby lépe odpovídal jeho rozptylu, což zlepšuje poměr signálu k šumu.

Subpásmový rozklad je klíčový pro efektivitu kodeku. Rozdělením spektra může algoritmus přidělovat bity jednotlivým subpásmům rozdílně podle jejich percepční důležitosti. Například u řeči lze více bitů přidělit nižším frekvenčním pásmům obsahujícím většinu fonetické informace, zatímco vyšším pásmům lze přidělit bitů méně. Toto zpracování ve frekvenční oblasti umožňuje efektivnější kompresi ve srovnání s plnopásmovou ADPCM. Dekodér provádí inverzní proces: ADPCM bitový proud každého subpásma je dekódován pro rekonstrukci subpásmového signálu a následně jsou subpásma syntetizována bankou filtrů za účelem vytvoření výsledného výstupního audio signálu.

SB-ADPCM je definován ve specifikacích 3GPP primárně pro hlasové a audio služby v mobilních sítích. Podporuje různé přenosové rychlosti, což nabízí kompromis mezi spotřebou šířky pásma a věrností zvuku. Kodek zahrnuje mechanismy pro zpracování ticha, tónových signálů a generování komfortního šumu, aby byla zachována přirozená kvalita konverzace při nespojitém přenosu ([DTX](/mobilnisite/slovnik/dtx/)). Jeho návrh je zaměřen na dostatečnou výpočetní efektivitu pro implementaci v reálném čase na hardwaru mobilních zařízení, přičemž poskytuje lepší kvalitu než jednodušší vlnové kodeky, jako je standardní PCM, při stejné nebo nižší přenosové rychlosti.

V rámci ekosystému 3GPP může být SB-ADPCM specifikován jako volba pro určité mediální komponenty ve službě multimediálních zpráv ([MMS](/mobilnisite/slovnik/mms/)), v systémech hlasové pošty nebo jiných streamovacích službách. Jeho úlohou je poskytnout standardizovaný kodek střední složitosti, který poskytuje dobrou audio kvalitu pro všeobecné aplikace bez extrémních výpočetních nároků pokročilejších percepčních kodeků, jako je [AMR-WB](/mobilnisite/slovnik/amr-wb/) nebo [EVS](/mobilnisite/slovnik/evs/), které jsou optimalizovány pro nejvyšší kvalitu při velmi nízkých přenosových rychlostech.

## K čemu slouží

SB-ADPCM byl vyvinut pro řešení potřeby efektivní digitální audio komprese v telekomunikacích, která vyvažuje kvalitu, přenosovou rychlost a výpočetní složitost. Před jeho přijetím systémy často používaly standardní [PCM](/mobilnisite/slovnik/pcm/) (např. G.711), které nabízí vysokou kvalitu, ale spotřebovává značnou šířku pásma (64 kbps), nebo jednoduchou ADPCM (např. G.726), která šířku pásma sice redukuje, ale nemusí optimálně zvládat spektrální charakteristiky audia. Motivací bylo vytvořit kodek, který by mohl poskytnout lepší percepční kvalitu než plnopásmová ADPCM při podobných přenosových rychlostech využitím vlastností lidského sluchu.

Historický kontext zahrnuje vývoj digitálních hlasových kodeků pro pevné a mobilní sítě. Jak se služby rozšiřovaly za hranice čisté hlasové komunikace a zahrnovaly multimediální zprávy a audio streamování, vznikla potřeba univerzálního kodeku, který by dokázal zpracovávat obecné audio, nikoli pouze řeč, s rozumnou efektivitou. SB-ADPCM zaplňuje mezeru mezi kodeky s nízkou přenosovou rychlostí určenými specificky pro řeč (jako je rodina AMR) a obecnými audio kodeky s vysokou kvalitou a vysokou přenosovou rychlostí. Řeší problém potřeby přijatelné audio kvality pro služby, kde je šířka pásma omezená, ale signál nemusí být čistě hlasový, jako je hudba při čekání nebo jednoduché audio klipy.

Odstranil omezení předchozích přístupů aplikací zpracování ve frekvenční oblasti. Plnopásmová ADPCM zachází se všemi frekvencemi stejně, což není optimální. Použitím subpásem umožňuje SB-ADPCM určitou formu percepčního kódování, kde lze kvantizační šum tvarovat tak, aby byl méně slyšitelný, čímž se zlepšuje vnímaná kvalita při dané datové rychlosti. To jej učinilo vhodným pro řadu služeb definovaných 3GPP, které vyžadují spolehlivou audio kompresi.

## Klíčové vlastnosti

- Využívá subpásmovou filtraci (např. QMF banku) k rozdělení audio signálu
- Aplikuje nezávislé ADPCM kódování na každé subpásmo
- Používá adaptivní kvantizaci s dynamickým nastavením kroku
- Podporuje proměnné přenosové rychlosti pro kompromisy mezi kvalitou a šířkou pásma
- Obsahuje funkce pro nespojitý přenos a komfortní šum
- Poskytuje lepší percepční kvalitu než plnopásmová ADPCM při srovnatelných přenosových rychlostech

## Související pojmy

- [ADPCM – Adaptive Differential Pulse Coded Modulation](/mobilnisite/slovnik/adpcm/)
- [QMF – Quadrature Mirror Filter](/mobilnisite/slovnik/qmf/)
- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)
- [PCM – Pulse Code Modulation](/mobilnisite/slovnik/pcm/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling

---

📖 **Anglický originál a plná specifikace:** [SB-ADPCM na 3GPP Explorer](https://3gpp-explorer.com/glossary/sb-adpcm/)
