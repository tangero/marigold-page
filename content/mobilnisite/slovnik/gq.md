---
slug: "gq"
url: "/mobilnisite/slovnik/gq/"
type: "slovnik"
title: "GQ – Global Quality"
date: 2025-01-01
abbr: "GQ"
fullName: "Global Quality"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gq/"
summary: "Komplexní metrika kvality hlasové nebo video konverzace od konce ke konci, definovaná v 3GPP. Reprezentuje celkovou uživatelsky vnímanou kvalitu integrací různých degradačních faktorů v celé přenosové"
---

GQ je komplexní metrika kvality hlasu nebo videa od konce ke konci, která reprezentuje celkovou uživatelsky vnímanou kvalitu integrací degradačních faktorů v celé přenosové cestě.

## Popis

Global Quality (GQ) je standardizovaná, objektivní metrika percepční kvality specifikovaná v 3GPP TS 26.935. Poskytuje jednu číselnou hodnotu, která predikuje celkovou kvalitu konverzační hlasové nebo video služby tak, jak ji vnímá koncový uživatel. Na rozdíl od metrik měřících kvalitu v izolovaných částech sítě (např. ztráta paketů v rádiovém spoji) se GQ snaží modelovat kumulativní efekt všech degradací kvality od úst jednoho uživatele k uším druhého uživatele (nebo od kamery k displeji). Jedná se o instrumentální, výpočetní metriku, což znamená, že je algoritmicky vypočítávána z měřitelných parametrů sítě a terminálu, nikoli prostřednictvím subjektivního lidského testování pro každé volání.

Výpočet GQ je založen na metodologii E-modelu, rozšířené a přizpůsobené pro úplné konverzační scénáře. Integruje širokou škálu vstupních parametrů, které přispívají ke zhoršení kvality. Mezi ně patří degradace specifické pro kodek (např. od [AMR](/mobilnisite/slovnik/amr/), [EVS](/mobilnisite/slovnik/evs/)), degradace způsobené zpožděním (zpoždění od úst k uším, včetně zpracování kodekem, kolísání zpoždění v síti a zpoždění vyrovnávací paměti pro přehrávání), degradace zařízení (od terminálů jako jsou telefony) a různé degradace na paketové vrstvě běžné v IP sítích. Poslední jmenované zahrnují ztrátu paketů (náhodnou i shlukovou), kolísání zpoždění paketů (jitter) a efekty algoritmů pro maskování chyb používaných kodekem při ztrátě nebo opoždění paketů.

Výstupem je skalární hodnota, často mapovaná na stupnici Mean Opinion Score ([MOS](/mobilnisite/slovnik/mos/)) (např. od 1 do 5), která poskytuje intuitivní odhad spokojenosti uživatele. Model GQ je navržen tak, aby byl použitelný pro účely plánování, kdy síťoví inženýři mohou zadávat očekávané rozsahy parametrů pro predikci kvality služby, a pro monitorování/assurance, kdy skutečné naměřené parametry ze živé sítě mohou být vloženy do modelu pro vyhodnocení kvality probíhajících hovorů. Jeho povaha od konce ke konci z něj činí cenný nástroj pro poskytovatele služeb k zaručení konzistentní úrovně kvality napříč heterogenními síťovými doménami (např. rádiový přístup, core, tranzitní sítě).

## K čemu slouží

GQ bylo vytvořeno, aby řešilo výzvu řízení a predikce kvality v stále složitějších, paketově přepínaných a více-dodavatelských komunikačních sítích. Před jeho standardizací bylo hodnocení kvality často fragmentované. Operátoři sítí mohli sledovat kvalitu rádiového spoje, latenci core sítě a ztrátu paketů odděleně, ale postrádali jednotnou metriku, která by dokázala přesně predikovat konečný uživatelský zážitek z konverzační služby. To ztěžovalo správu smluv o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) od konce ke konci a řešení problémů.

S přechodem od přepojování okruhů pro hlas (kde byla kvalita relativně stabilní) k Voice over IP (VoIP) a později Voice over LTE (VoLTE) a Voice over NR (VoNR) se dominantními staly nové degradační faktory jako proměnlivé zpoždění, jitter a ztráta paketů. Účelem GQ, zavedeného v Rel-8 spolu s raným vývojem hlasu založeného na IMS, bylo poskytnout standardizovaný, objektivní nástroj, který by dokázal modelovat tyto kombinované efekty. Umožňuje operátorům plánovat sítě (dimenzování výběru kodeku, rozpočty zpoždění, cíle pro ztráty) pro dosažení požadované úrovně kvality a monitorovat živé sítě, aby identifikovali, zda se skutečná kvalita odchyluje od predikcí, což spustí vyšetřování, který segment sítě degradaci způsobuje.

## Klíčové vlastnosti

- Predikce kvality od konce ke konci integrující všechny degradace konverzační služby
- Založeno na rozšířené metodologii E-modelu pro výpočetní efektivitu
- Zohledňuje degradaci kodeku, zpoždění, kvalitu zařízení a efekty ztráty paketů
- Výstupem je skalární hodnota typicky mapovaná na stupnici Mean Opinion Score (MOS)
- Použitelné jak pro plánování/návrh sítě, tak pro monitorování živé služby
- Standardizovaný algoritmus zajišťuje konzistentní měření napříč různými dodavateli a sítěmi

## Definující specifikace

- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia

---

📖 **Anglický originál a plná specifikace:** [GQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/gq/)
