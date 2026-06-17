---
slug: "c-sgn"
url: "/mobilnisite/slovnik/c-sgn/"
type: "slovnik"
title: "C-SGN – CIoT Serving Gateway Node"
date: 2025-01-01
abbr: "C-SGN"
fullName: "CIoT Serving Gateway Node"
category: "IoT"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/c-sgn/"
summary: "C-SGN je kombinovaný síťový uzel pro Cellular IoT (CIoT), který integruje funkce MME a S-GW. Zjednodušuje architekturu jádra sítě pro nasazení IoT, snižuje signalizační režii a je optimalizován pro za"
---

C-SGN je kombinovaný síťový uzel pro CIoT, který integruje funkce MME a S-GW za účelem zjednodušení architektury jádra sítě a optimalizace pro zařízení IoT s nízkou spotřebou.

## Popis

CIoT Serving Gateway Node (C-SGN) je specializovaná síťová entita zavedená organizací 3GPP jako součást Cellular IoT (CIoT) EPS Optimalizací. Jedná se o konvergovaný uzel, který spojuje funkce tradičně vykonávané dvěma samostatnými entitami jádra sítě: Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) a Serving Gateway (S-GW). Tato architektonická konvergence je navržena speciálně pro splnění jedinečných požadavků zařízení IoT, která se vyznačují přenosy malých objemů dat, občasnou komunikací a potřebou extrémní energetické účinnosti.

Z architektonického hlediska se C-SGN nachází v rámci Evolved Packet Core (EPC) a komunikuje s CIoT podporujícími základnovými stanicemi (eNodeB) přes rozhraní S1-MME a S1-U, stejně jako by to dělaly samostatné MME a S-GW. Konsolidací těchto rolí do jednoho uzlu se však eliminuje vnitřní signalizace a správa stavů mezi řídicí rovinou (MME) a uživatelskou rovinou (S-GW). Tato vnitřní integrace umožňuje efektivnější zpracování procedur specifických pro CIoT, jako je připojení (Attach) s nebo bez připojení k PDN, a zpracování dat prostřednictvím CIoT EPS Optimalizace přes řídicí rovinu nebo přes uživatelskou rovinu.

Při provozu C-SGN spravuje celý životní cyklus připojení CIoT UE. Vykonává funkce správy mobility, jako je správa oblastí sledování (tracking area) a autentizace, a zároveň zajišťuje funkce brány spočívající v ukotvení uživatelské roviny, správě EPS přenosových kanálů (i když je často pro IoT zjednodušena) a fungování jako lokální kotva mobility při předávání mezi eNodeB. Pro přenos dat podporuje klíčové funkce CIoT: přenos malých datových paketů přes řídicí rovinu pomocí Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) (což eliminuje potřebu zřizování datového přenosového kanálu) a efektivní přenos dat uživatelské roviny s podporou komprese hlaviček. Také komunikuje s Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)) nebo přímo s aplikačními platformami přes rozhraní SGi při použití Service Capability Exposure Function (SCEF) pro doručování ne-IP dat ([NIDD](/mobilnisite/slovnik/nidd/)).

Jeho role v síti je klíčová pro škálovatelné a nákladově efektivní služby IoT. Snížením počtu síťových uzlů a mezilehlé signalizace snižuje náklady na nasazení a provozní složitost pro síťové operátory zaměřené na trh IoT. Optimalizuje síťovou cestu pro malé datové pakety, minimalizuje latenci a spotřebu prostředků na transakci, což přímo přispívá k prodloužení životnosti baterií zařízení IoT. C-SGN je základní komponentou umožňující masivní konektivitu, ultra nízké náklady a energeticky účinný provoz, které jsou charakteristickými znaky vize CIoT podle 3GPP.

## K čemu slouží

C-SGN byl vytvořen, aby řešil základní nesoulad mezi tradiční architekturou EPC pro mobilní širokopásmový přístup a požadavky zařízení Cellular IoT. Standardní EPC se samostatnými [MME](/mobilnisite/slovnik/mme/) a S-GW je optimalizována pro nepřetržité nebo časté datové relace, složitou mobilitu a vysoké přenosové rychlosti – charakteristiky opačné k těm, které mají většina IoT aplikací. Zařízení IoT typicky přenášejí velmi malá množství dat občasně, zůstávají stacionární nebo se pohybují zřídka a musí fungovat roky na jedné baterii. Režie spojená se zřizováním a udržováním plných přenosových kanálů uživatelské roviny mezi S-GW a [P-GW](/mobilnisite/slovnik/p-gw/) pro každý malý datový paket je neúměrně neefektivní, spotřebovává nadměrnou energii zařízení a síťové prostředky.

Historickým kontextem jeho zavedení ve verzi 13 (Release 13) byl soustředěný úsilí 3GPP učinit sítě LTE konkurenceschopnou platformou pro rychle rostoucí trh IoT, který soupeřil s necelulárními technologiemi jako LoRa a Sigfox. Pracovní položka CIoT EPS Optimalizací měla za cíl snížit signalizační režii, snížit spotřebu energie zařízení a podporovat masivní počty zařízení. Klíčovou částí této optimalizace bylo zjednodušení architektury jádra sítě. Samostatný model MME a S-GW zahrnoval významnou signalizaci (např. zprávy [GTP-C](/mobilnisite/slovnik/gtp-c/)) pro správu přenosových kanálů, a to i pro minimální objem dat. Kombinací těchto funkcí je tato vnitřní signalizace eliminována a procedury mohou být zjednodušeny specificky pro charakter provozu IoT.

C-SGN tedy řeší problémy síťové neefektivity a vysokých nákladů na připojení IoT. Snižuje kapitálové výdaje operátorů tím, že umožňuje nasazení jednoho integrovaného uzlu místo dvou. Snižuje provozní signalizační zátěž sítě. Nejvýznamněji však umožňuje funkce CIoT EPS Optimalizací, jako je přenos dat přes řídicí rovinu a efektivní zpracování uživatelské roviny, které drasticky snižují procedury v rádiovém rozhraní a síti potřebné k odeslání dat zařízením IoT, čímž řeší kritický problém nadměrné spotřeby energie zařízení. Jeho vytvoření bylo motivováno potřebou přizpůsobit výkonný systém LTE tak, aby byl životaschopný pro nasazení IoT s nízkými náklady, nízkou spotřebou a masivním měřítkem.

## Klíčové vlastnosti

- Integrace funkcí MME a S-GW do jednoho síťového uzlu
- Podpora CIoT EPS Optimalizace přes řídicí rovinu (přenos dat přes NAS)
- Podpora CIoT EPS Optimalizace přes uživatelskou rovinu s efektivní správou přenosových kanálů
- Správa mobility a stavů připojení CIoT UE
- Rozhraní s SCEF pro doručování ne-IP dat (NIDD)
- Optimalizované signalizační procedury pro připojování (Attach) a přenos dat zařízení IoT

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.720** (Rel-13) — Cellular IoT Architecture Enhancement Study

---

📖 **Anglický originál a plná specifikace:** [C-SGN na 3GPP Explorer](https://3gpp-explorer.com/glossary/c-sgn/)
