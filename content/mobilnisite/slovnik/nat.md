---
slug: "nat"
url: "/mobilnisite/slovnik/nat/"
type: "slovnik"
title: "NAT – Network Address Translation"
date: 2026-01-01
abbr: "NAT"
fullName: "Network Address Translation"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nat/"
summary: "Metoda přemapování IP adresních prostorů používaná v sítích 3GPP k úspoře veřejných IPv4 adres a zajištění soukromí. Překládá privátní IP adresy používané v mobilní síti na veřejné adresy pro komunika"
---

NAT je metoda přemapování IP adresních prostorů v sítích 3GPP, která překládá privátní IP adresy na veřejné adresy za účelem úspory veřejných IPv4 adres a umožnění masivního připojení.

## Popis

Network Address Translation (NAT) v sítích 3GPP je funkce typicky implementovaná v bráně Packet Data Network Gateway (PGW) v 4G nebo ve funkci User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5G. Působí na IP vrstvě a mění zdrojové a/nebo cílové IP adresy (a často i čísla portů) v hlavičkách paketů při jejich přenosu mezi uživatelským zařízením (UE) a externími paketovými datovými sítěmi (PDN), jako je internet. Základní mechanismus spočívá v udržování NAT vazební tabulky, která mapuje privátní IP adresu každého UE (přidělenou z poolu mobilního operátora, např. 10.0.0.0/8) a zdrojový port na unikátní veřejnou IP adresu a port na externím rozhraní. Pro odchozí pakety z UE funkce NAT nahradí privátní zdrojovou IP adresu a port namapovanými veřejnými; pro příchozí pakety určené pro UE provede reverzní překlad na základě cílového portu a IP adresy v paketu.

Architektura integruje NAT do datové cesty v uživatelské rovině. V EPS (4G) slouží PGW jako kotvicí bod a provádí NAT pro PDN připojení, která to vyžadují, často je konfigurována jako součást kontextu Packet Data Protocol (PDP) nebo při vytváření PDN připojení. V 5GC provádí ekvivalentní funkci bodu přítomnosti N6 UPF. Mezi klíčové komponenty patří NAT mapovací tabulka (stav), časovače pro správu životnosti neaktivních mapování a algoritmy pro přidělování portů (např. Port Address Translation - PAT). Pokročilé formy jako Carrier-Grade NAT (CGN) nebo Large Scale NAT (LSN) se používají k mapování tisíců UE na jedinou nebo malý pool veřejných IPv4 adres s využitím rozsahů portů pro rozlišení toků.

Role NAT je mnohostranná: šetří globálně nedostatkový prostor IPv4 adres tím, že umožňuje mnoha UE sdílet několik veřejných adres; přidává vrstvu soukromí a základní zabezpečení skrytím interní topologie sítě; a zjednodušuje správu sítě pro operátory. Zároveň však zavádí složitosti a porušuje end-to-end princip internetu. Může interferovat s protokoly, které vkládají IP adresy do datové části (např. SIP, [FTP](/mobilnisite/slovnik/ftp/)), pokud nejsou doprovázeny Application Layer Gateways (ALG) nebo technikami jako NAT Traversal ([NAT-T](/mobilnisite/slovnik/nat-t/)). V rámci 3GPP je chování a konfigurace NAT specifikována tak, aby zajistila interoperabilitu a předvídatelné poskytování služeb napříč různými zařízeními dodavatelů a nasazeními sítí.

## K čemu slouží

NAT byl v sítích 3GPP přijat primárně pro zmírnění vyčerpání veřejných IPv4 adres, což je kritický problém, který se objevil s explozivním růstem mobilních internetových zařízení. Bez NAT by každé UE vyžadující přístup k internetu potřebovalo unikátní veřejnou IPv4 adresu, což je požadavek neudržitelný vzhledem k omezenému adresnímu prostoru. NAT to řeší tím, že umožňuje operátorům používat interně velké privátní adresní prostory (RFC 1918) a mapovat je na mnohem menší pool veřejných adres. To umožnilo nákladově efektivní škálování služeb mobilního širokopásmového připojení od 3G (R99) dále.

Historicky měly rané mobilní datové služby omezené měřítko a někdy používaly veřejné adresování. S rozšiřováním služeb se NAT stal nezbytnou síťovou funkcí. Jeho integrace do standardů 3GPP zajistila konzistentní, mezi dodavateli interoperabilní přístup k úspoře adres. Dále NAT poskytl vedlejší výhody, jako je základní firewallový efekt, protože nevyžádaný příchozí provoz bez existujícího mapování je typicky zahazován, což zvyšuje zabezpečení sítě. Tato technologie řešila omezení pouhého nasazení IPv6 (které má adres nadbytek) tím, že poskytla okamžité, zpětně kompatibilní řešení, zatímco přechod na IPv6 postupoval pomalu. Účel NAT se vyvinul také k podpoře síťových architektur, jako je konvergence pevných a mobilních sítí a multi-homing, kde je provoz z různých typů přístupu agregován prostřednictvím společné brány provádějící NAT.

## Klíčové vlastnosti

- Překládá privátní IPv4 adresy na veřejné IPv4 adresy (a naopak)
- Implementuje Port Address Translation (PAT) pro multiplexování mnoha uživatelů na jednu IP adresu
- Udržuje stavové mapovací tabulky s konfigurovatelnými politikami časového limitu
- Integrován do brán jádrové sítě (GGSN/PGW/UPF) pro mobilní provoz
- Může být nasazen jako Carrier-Grade NAT (CGN) pro agregaci rozsáhlého počtu účastníků
- Podporuje různé varianty NAT, jako je full-cone, restricted-cone, port-restricted a symmetric

## Související pojmy

- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TR 22.832** (Rel-17) — Study on cyber-physical control in vertical domains
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 23.875** (Rel-5) — Feasibility Study for Push Services Architecture
- **TR 23.981** (Rel-19) — IPv4 IMS Interworking and Migration Study
- … a dalších 35 specifikací

---

📖 **Anglický originál a plná specifikace:** [NAT na 3GPP Explorer](https://3gpp-explorer.com/glossary/nat/)
