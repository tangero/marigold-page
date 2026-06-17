---
slug: "mvegc"
url: "/mobilnisite/slovnik/mvegc/"
type: "slovnik"
title: "MVEGC – MCVideo Emergency Group Call"
date: 2025-01-01
abbr: "MVEGC"
fullName: "MCVideo Emergency Group Call"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mvegc/"
summary: "Služba skupinového video hovoru v reálném čase v rámci MCVideo, aktivovaná při mimořádných událostech, která umožňuje interaktivní video komunikaci mezi členy skupiny MCVideo Emergency Group. Umožňuje"
---

MVEGC je služba skupinového video hovoru v reálném čase v rámci MCVideo, která je aktivována při mimořádných událostech a umožňuje interaktivní video komunikaci mezi členy skupiny MCVideo Emergency Group.

## Popis

[MCVideo](/mobilnisite/slovnik/mcvideo/) Emergency Group Call (MVEGC) je standardizovaná služba v portfoliu Mission Critical Video (MCVideo) konsorcia 3GPP, která usnadňuje interaktivní, mnohostrannou video komunikaci mezi členy určené nouzové skupiny. Na rozdíl od jednosměrného vysílání služby [MVEA](/mobilnisite/slovnik/mvea/) podporuje MVEGC obousměrný video přenos, což umožňuje více účastníkům současně odesílat a přijímat živé video, podobně jako u videokonference, ale uzpůsobené pro nouzové scénáře. Službu zahajuje autorizovaný uživatel, typicky velitel zásahu, a cílí na konkrétní skupinu MCVideo Emergency Group ([MVEG](/mobilnisite/slovnik/mveg/)). Využívá jádro IMS pro řízení relace a aplikační server MCVideo pro správu hovoru, přičemž používá sítě LTE nebo 5G s prioritním QoS, aby zajistila nízkou latenci a vysokou spolehlivost.

Z architektonického hlediska se na MVEGC podílí několik klíčových komponent pracujících společně. Klient MCVideo na uživatelském zařízení podporuje funkce pro připojení ke skupinovým hovorům, správu kódování/dekódování videa a obsluhu uživatelského rozhraní pro řízení práva vysílat (tj. určování, kdo může v daném okamžiku mluvit nebo sdílet video). Aplikační server MCVideo řídí hovor tím, že autentizuje iniciátora, ověřuje členství v cílové skupině MVEG a zřizuje multimediální relaci prostřednictvím IMS. Rozhraní s funkcemi pro zpracování médií (např. Media Resource Function Processor) zajišťuje mixování videa nebo selektivní přeposílání, v závislosti na architektuře – buď centralizovaný mixér pro optimalizaci šířky pásma, nebo síťový (mesh) přístup pro přímý přenos mezi zařízeními v lokalizovaných scénářích. Síť zajišťuje vyhrazené přenosové kanály s vysokou prioritou, často s využitím hodnot QoS Class Identifier ([QCI](/mobilnisite/slovnik/qci/)) určených pro služby kritické pro plnění misí.

Fungování MVEGC začíná zahájením hovoru. Iniciátor vybere skupinu MVEG a spustí žádost o skupinový hovor, která je signalizována na server MCVideo pomocí SIP přes IMS. Server ověří oprávnění a získá seznam členů skupiny ze systému správy skupin. Poté rozešle pozvánky na zařízení každého člena a zřídí jednotlivé RTP toky pro video a audio. Mechanismy řízení práva vysílat, které mohou být založeny na prioritě mluvčího nebo na protokolu žádost-povolení, spravují, které video účastníka je prominentně zobrazeno nebo přeposíláno ostatním. Hovor může být přednostní, což znamená, že může přerušit jinou komunikaci, a typicky zahrnuje funkce jako nouzová indikace a sdílení polohy. Úloha MVEGC v síti spočívá v poskytování standardizované, interoperabilní platformy pro společnou video komunikaci během mimořádných událostí, která umožňuje vizuální koordinaci v reálném čase, klíčovou pro složité zásahové operace, jako je pátrací a záchranná akce nebo taktické policejní zásahy.

## K čemu slouží

MVEGC byl vyvinut, aby zaplnil mezeru v interaktivní vizuální komunikaci pro zásahové týmy, kde skupinové hovory pouze s hlasem (jako tradiční [MCPTT](/mobilnisite/slovnik/mcptt/)) omezují pochopení situace. Před jeho zavedením byly video komunikace pro veřejnou bezpečnost často proprietární, nestandardizované nebo omezené na point-to-point spojení, což bránilo skupinové koordinaci. Mezi omezení patřila neschopnost současně sdílet více živých video perspektiv, což vedlo k roztříštěnému povědomí o situaci a opožděnému rozhodování v rychle se vyvíjejících incidentech. Motivací pro MVEGC byla rostoucí dostupnost zařízení s podporou videa a širokopásmových sítí spolu s požadavky orgánů veřejné bezpečnosti na nástroje napodobující osobní spolupráci na dálku.

Historicky se skupinová komunikace při mimořádných událostech spoléhala na hlasové radiostanice, které, ač efektivní pro zvuk, nedokázaly přenést vizuální detaily, jako je poškození konstrukce, stav obětí nebo vzhled podezřelých. Vývoj směrem k službám Mission Critical Services založeným na LTE vytvořil základ pro multimédia, ale počáteční fáze se zaměřovaly na push-to-talk. MVEGC řeší problém umožnění koordinovaného, víceúčastnického video dialogu během mimořádných událostí, což umožňuje zasahujícím jednotkám sdílet vizuální informace v reálném čase ze svých perspektiv. To zlepšuje kolektivní povědomí o situaci, snižuje nesprávné interpretace a podporuje informovanější velitelská rozhodnutí, což může zlepšit výsledky v život ohrožujících situacích.

Vytvoření MVEGC bylo hnáno spoluprací 3GPP se zainteresovanými stranami z oblasti veřejné bezpečnosti na definování komplexních standardů pro video služby kritické pro plnění misí. Integruje se s existujícími komponentami [MCS](/mobilnisite/slovnik/mcs/), čímž zajišťuje zpětnou kompatibilitu a jednotnou správu. Standardizací MVEGC umožňuje 3GPP interoperabilitu mezi různými dodavateli a sítěmi, což je zásadní pro společné operace zahrnující více agentur nebo zemí. Představuje významný pokrok oproti předchozím přístupům tím, že využívá sítě založené na IP k poskytování interaktivního skupinového videa se spolehlivostí a prioritou vyžadovanou pro zásahové operace, s konečným cílem zachraňovat životy díky vylepšené komunikaci.

## Klíčové vlastnosti

- Interaktivní mnohostranné (many-to-many) video volání mezi členy skupiny MCVideo Emergency Group
- Mechanismy řízení práva vysílat pro správu práv k přenosu videa mezi účastníky
- Integrace s IMS pro zřizování relace a přenosové kanály médií s podporou QoS
- Přednostní (preemptivní) schopnosti hovoru pro přerušení nehavarijní komunikace
- Podpora živého video přenosu s profily nízké latence a vysoké spolehlivosti
- Spolupráce s dalšími službami MCS, jako je MCPTT, pro kombinované hlasové/video operace

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MVEGC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mvegc/)
