---
slug: "pat"
url: "/mobilnisite/slovnik/pat/"
type: "slovnik"
title: "PAT – Program Association Table"
date: 2025-01-01
abbr: "PAT"
fullName: "Program Association Table"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pat/"
summary: "Datová struktura v MPEG-2 transportním proudu používaná k asociaci čísel programů s jejich odpovídajícími tabulkami map programů (PMT). Je zásadní pro digitální vysílání a multimediální streamovací sl"
---

PAT (Program Association Table) je tabulka asociací programů, základní datová struktura v MPEG-2 transportním proudu, která asociuje čísla programů s jejich odpovídajícími tabulkami map programů (PMT), aby umožnila přijímači lokalizovat a dekódovat konkrétní komponenty programu.

## Popis

Program Association Table (PAT) je povinná tabulka definovaná ve specifikaci [MPEG-2](/mobilnisite/slovnik/mpeg-2/) Systems ([ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 13818-1) a přijatá 3GPP pro multimediální vysílání a streamovací služby, jako je [MBMS](/mobilnisite/slovnik/mbms/) (Multimedia Broadcast Multicast Service) a pozdější vylepšení. Nachází se v paketech s Packet ID ([PID](/mobilnisite/slovnik/pid/)) 0 v rámci MPEG-2 transportního proudu (TS). Primární funkcí PAT je sloužit jako kořenový adresář pro TS. Poskytuje mapování mezi každým číslem programu (jednoznačný identifikátor programu nebo služby v multiplexu) a hodnotou PID paketů transportního proudu, které nesou odpovídající Program Map Table ([PMT](/mobilnisite/slovnik/pmt/)) pro daný program.

Z architektonického hlediska je PAT první tabulkou, kterou musí dekodér analyzovat při naladění na transportní proud. TS je multiplex mnoha elementárních proudů (video, audio, data) patřících k jednomu nebo více programům. Bez PAT by přijímač nevěděl, kde najít popisy těchto programů. PAT funguje tak, že je v TS periodicky vysílána. Když přijímač filtruje PID 0, extrahuje data PAT. Tato data jsou jednoduchým seznamem čísel programů a jejich přidružených PMT_PID. Pro číslo programu 0 odkazuje přidružený PID na Network Information Table ([NIT](/mobilnisite/slovnik/nit/)), která obsahuje informace o fyzické síti.

Jakmile je PAT dekódována, může přijímač vybrat požadované číslo programu a následně filtrovat TS pro pakety s PID určeným pro PMT tohoto programu. PMT poté uvádí všechny komponentní proudy (s jejich PID a typy proudů), které tvoří vybraný program, což umožňuje dekodéru sestavit audio, video a další data. V kontextu 3GPP je tento mechanismus klíčový pro služby jako eMBMS (evolved MBMS), kde je vysílací obsah doručován přes sítě LTE nebo 5G. PAT umožňuje efektivní objevování a výběr služeb v rámci vysílací/multicastové relace, což uživatelskému zařízení umožňuje správně se naladit a dekódovat zamýšlenou vysílací službu z multiplexovaného transportního proudu doručovaného přes rozhraní vzduchu.

## K čemu slouží

PAT existuje, aby vyřešila základní problém objevování služeb a demultiplexování v paketizovaném, multiplexovaném prostředí transportního proudu. V digitálním vysílání a streamování je více televizních kanálů, rozhlasových programů a datových služeb sloučeno do jediného přenosového bitového proudu, aby byla maximalizována efektivita šířky pásma. Bez definovaného indexovacího mechanismu, jako je PAT, by přijímač neměl způsob, jak identifikovat, které pakety patří ke kterému programu, což by znemožnilo selektivní naladění. Poskytuje základní 'obsah' pro celý multiplex.

Její vytvoření bylo motivováno přechodem z analogového na digitální vysílání a potřebou standardizovaného, flexibilního multiplexního schématu. Vrstva [MPEG-2](/mobilnisite/slovnik/mpeg-2/) Systems, která zahrnuje PAT, byla navržena tak, aby byla nezávislá na síti, fungovala přes satelitní, kabelové, pozemní a později mobilní sítě. 3GPP tento model přijala pro MBMS, aby využila dobře pochopený, robustní mechanismus pro popis služeb, což umožnilo poskytování vysílacích TV a rozhlasových služeb přes mobilní sítě. Tím se vyřešilo omezení dřívějších mobilních vysílacích technologií, kterým chybělo takové standardizované, škálovatelné rámcové řešení na úrovni služeb.

V kontextu 3GPP PAT umožňuje efektivní využití vzácných rádiových zdrojů pro vysílací služby. Tím, že umožňuje multiplexovat více služeb do jediného vysílacího nosiče, je optimalizována kapacita sítě. PAT umožňuje uživatelskému zařízení rychle najít a dekódovat pouze službu, o kterou má zájem, bez nutnosti zpracovávat celý multiplex, čímž šetří energii baterie a výpočetní zdroje. Je klíčovým prvkem pro lineární vysílací služby, streamování živých událostí a softwarové aktualizace přes vzduch pomocí vysílání, čímž tvoří základní vrstvu služeb pro doručování typu point-to-multipoint v mobilních sítích.

## Klíčové vlastnosti

- Nachází se v paketech MPEG-2 transportního proudu s PID 0
- Mapuje čísla programů na hodnoty PID jejich příslušných tabulek map programů (PMT)
- Obsahuje položku pro číslo programu 0, která odkazuje na Network Information Table (NIT)
- Přenáší se periodicky, aby byl zajištěn rychlý příjem služeb přijímači
- Povinná tabulka pro jakýkoli MPEG-2 transportní proud
- Umožňuje selektivní dekódování konkrétních programů z multiplexu

## Související pojmy

- [PMT – Program Map Table](/mobilnisite/slovnik/pmt/)

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [PAT na 3GPP Explorer](https://3gpp-explorer.com/glossary/pat/)
