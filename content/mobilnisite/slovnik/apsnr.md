---
slug: "apsnr"
url: "/mobilnisite/slovnik/apsnr/"
type: "slovnik"
title: "APSNR – Average Peak Signal-to-Noise Ratio"
date: 2025-01-01
abbr: "APSNR"
fullName: "Average Peak Signal-to-Noise Ratio"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/apsnr/"
summary: "APSNR je metrika kvality videa standardizovaná organizací 3GPP pro hodnocení percepční kvality kódovaných video toků. Poskytuje objektivní, kvantitativní měřítko věrnosti videa průměrováním hodnot PSN"
---

APSNR je standardizovaná metrika kvality videa podle 3GPP, která průměruje hodnoty PSNR napříč snímky videa, aby poskytla objektivní měřítko věrnosti videa pro hodnocení výkonu doručování a QoE.

## Popis

Průměrný poměr signálu k šumu (Average Peak Signal-to-Noise Ratio, APSNR) je standardizovaná objektivní metrika pro hodnocení kvality videa definovaná v dokumentu 3GPP TS 26.902. Funguje tak, že vypočítá poměr signálu k šumu ([PSNR](/mobilnisite/slovnik/psnr/)) pro jednotlivé video snímky nebo sekvence a následně spočítá průměrnou hodnotu napříč hodnoceným obsahem. Samotný PSNR je matematické porovnání mezi původním (referenčním) videosignálem a zpracovanou nebo degradovanou verzí, vyjádřené v decibelech (dB). Vyšší hodnoty APSNR indikují lepší kvalitu videa, protože signalizují nižší zkreslení a šum vzhledem k původnímu signálu.

Technicky výpočet APSNR zahrnuje několik kroků. Nejprve se vypočítá střední kvadratická chyba (Mean Squared Error, [MSE](/mobilnisite/slovnik/mse/)) mezi odpovídajícími pixely původního a zpracovaného video snímku. U barevného videa se to obvykle provádí samostatně pro složku jasu (Y) a barevné složky (Cb, Cr), přičemž složka jasu je často více vážena kvůli citlivosti lidského zraku. PSNR pro snímek se pak odvodí z MSE pomocí logaritmického vzorce, který zahrnuje maximální možnou hodnotu pixelu (např. 255 pro 8bitové video). APSNR je průměr těchto hodnot PSNR na snímek za stanovené časové období, například video klip nebo streamovací relaci.

V rámci architektury 3GPP se APSNR primárně využívá ve službě multimediální telefonie pro IMS ([MTSI](/mobilnisite/slovnik/mtsi/)) a dalších multimediálních servisních rámcích. Slouží jako klíčový ukazatel výkonu ([KPI](/mobilnisite/slovnik/kpi/)) pro hodnocení výkonu videokodeků, plánování sítě a monitorování kvality uživatelského prožitku ([QoE](/mobilnisite/slovnik/qoe/)). Metrika je integrována do testovacích metodologií a specifikací požadavků na výkon, což umožňuje konzistentní benchmarkování videokodeků jako H.264/[AVC](/mobilnisite/slovnik/avc/) a [HEVC](/mobilnisite/slovnik/hevc/) napříč různými implementacemi a síťovými podmínkami.

Ačkoli je APSNR výpočetně efektivní a široce srozumitelná, má omezení v dokonalé korelaci s lidským percepčním vjemem kvality, zejména u moderních videokodeků využívajících pokročilé kompresní techniky. Nicméně její standardizace v rámci 3GPP zajišťuje společnou, reprodukovatelnou metodu pro počáteční hodnocení kvality, která je často používána spolu s sofistikovanějšími percepčními metrikami, jako je VQM nebo [SSIM](/mobilnisite/slovnik/ssim/), pro komplexní analýzu kvality videa v mobilních sítích.

## K čemu slouží

APSNR byla zavedena, aby poskytla standardizovanou, objektivní metodu pro hodnocení kvality videa v rámci multimediálních služeb 3GPP. Před její standardizací se hodnocení kvality videa v mobilních sítích často spoléhalo na proprietární metriky nebo základní výpočty PSNR bez konzistentních metod průměrování, což ztěžovalo srovnání mezi různými dodavateli a benchmarkování výkonu. Vytvoření APSNR řešilo potřebu sjednocené, reprodukovatelné metriky, na kterou lze odkazovat napříč specifikacemi, testovacími plány a požadavky na shodu zařízení.

Primární problém, který APSNR řeší, je vytvoření společného technického jazyka pro měření věrnosti videa v ekosystému 3GPP. Jak se mobilní sítě vyvíjely, aby podporovaly pokročilé video služby jako videohovory, mobilní TV a streamování, operátoři a výrobci zařízení potřebovali spolehlivý způsob, jak kvantifikovat dopad video komprese, přenosových chyb a závad v síti na uživatelský prožitek. APSNR poskytuje tuto kvantitativní základnu, což umožňuje nastavení minimálních prahových hodnot kvality pro výkon kodeku a síťového doručování.

Historicky vycházela motivace pro standardizaci APSNR z rozšíření multimediálních služeb ve verzi 3GPP Release 8 a novějších. S přijetím služeb založených na IMS a vyšších přenosových kapacit se stalo zajištění konzistentní kvality videa klíčovým pro přijetí služeb. APSNR, jako přímočaré rozšíření dobře zavedeného konceptu PSNR, nabídla praktický kompromis mezi výpočetní jednoduchostí a smysluplnou indikací kvality, což usnadnilo její začlenění do standardů testování výkonu a nástrojů pro optimalizaci sítě.

## Klíčové vlastnosti

- Standardizovaná objektivní metrika kvality videa definovaná v 3GPP TS 26.902
- Vypočítává průměrný PSNR napříč video snímky nebo sekvencemi
- Poskytuje kvantitativní měření kvality v decibelech (dB)
- Podporuje hodnocení složek jasu a barevnosti
- Používá se pro benchmarkování výkonu videokodeků a testování shody
- Umožňuje konzistentní monitorování kvality uživatelského prožitku (QoE) pro multimediální služby

## Související pojmy

- [PSNR – Peak Signal-to-Noise Ratio](/mobilnisite/slovnik/psnr/)
- [MTSI – Multimedia Telephony Services for IMS](/mobilnisite/slovnik/mtsi/)
- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)

## Definující specifikace

- **TR 26.902** (Rel-19) — Video Codec Performance for 3GPP Packet Services

---

📖 **Anglický originál a plná specifikace:** [APSNR na 3GPP Explorer](https://3gpp-explorer.com/glossary/apsnr/)
