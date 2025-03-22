---
ID: 1090
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/wds-pro-pohodlnou-stavbu-vetsi-wifi-site

  '
post_date: 2004-04-27 07:03:00
post_excerpt: ''
published: true
summary_points:
- WDS propojuje bezdrátově přístupové body, eliminujíc ethernetové kabely.
- WDS snižuje rychlost WiFi sítě zhruba na polovinu.
- WDS není standardizovaný, proto je doporučeno používat zařízení stejného výrobce.
- WDS lze použít pro přemostění sítí nebo opakování signálu s omezeními.
title: WDS – pro pohodlnou stavbu větší WiFi sítě
---

<p>
Potřebujete propojit bezdrátově několik přístupových bodů? Udělat větší WiFi síť bez nutnosti každé AP připojovat do ethernetu? Pomůže WDS a zde se dočtete, jak.
</p>

<!--more--><p>
<p>
Tento článek je vlastně upgrade k mojí knize WiFi: Praktický průvodce. WDS v době, kdy jsem knihu psal, byla technologie v plenkách, proto jsem jí nemohl věnovat patřičnou pozornost, ještě nebylo vyzkošené a osahané, jak to funguje. Dnes už je to mnohem jasnější, takže tento článek si můžete vytisknout a vložit do knihy. Zdrojem byly materiály Intersilu, Proximu, Broadcomu a SmallNetBuilderu. </p>

<p>
Stavět bezdrátovou síť by bylo nepochybně mnohem jednodušší, kdyby bylo možno jednotlivé přístupové body (access pointy, AP) propojovat rovněž bezdrátovou sítí a nemuset mezi nimi tahat ethernetový kabel. Bohužel bezdrátové sítě na kabeláž coby "distribuční médium" dopravující k nim internet, značně spoléhají. Ale jistě nepochybujeme o tom, že by bylo mnohem pohodlnější a rychlejší, přivést internet jen do jednoho přístupového bodu a nechat přístupové body, aby si internet mezi sebou distribuovali vzduchem. </p>

<p>
Tak přesně tohle dělá systém WDS - ačkoliv s určitými omezeními, především pak rychlostními a kapacitními. WDS je v překladu <EM>Wireless Distribution System</EM>, bezdrátový distribuční systém. Jde o technologii, která umožní na stejném kanálu propojovat jednotlivé přístupové body a na stejném kanálu k nim také připojovat klientské adaptery. Už z toho vyplývá jisté omezení - část kapacity bezdrátové sítě (přibližně poloviční) schlamste samotná distribuce internetového signálu. Pokud tedy potřebujete rychlost WiFi využívat na maximum, není WDS pro vás, pokud vám stačí efektivní rychlost několika megabitů a oceníte jednoduchou a rychlou instalaci, bude vás WDS zajímat. Tento článek má za úkol popsat vám možnosti WDS a ukázat si, jak se s ním prakticky pracuje. </p>

<p>
Funkce podobná WDS se objevila již dříve v drahých přístupových bodech <EM>(v tomto článku považuji výraz přístupový bod za ekvivalent k širokopásmovému směrovači, routeru - protože i v něm je přístupový bod a to nás zajímá)</EM>, postupem doby ale funkce sestoupila i do nejlevnějších zařízení za několik tisícikorun. K tomu přispěl především výrobce čipových sad BroadCom, který podporu WDS do své čipové sady integroval. </p>

<p>
<STRONG>Upozornění: WDS není žádný standard</STRONG> a ačkoliv IEEE začíná na jeho standardizaci pracovat, zatím jde o uvolněný a nestandardizovaný koncept. Není tedy zaručeno, že jednotlivé výrobky různých výrobců označené WDS mezi sebou budou kooperovat, je vždy výhodnější nakoupit techniku u jednoho výrobce. Na druhou stranu, díky tomu, že WDS podporuje čipset Broadcom a firma dodává kódy s podporou, často se liší pouze terminologie, mohou být ale problémy s rozsahem a způsobem konfigurace. </p>

<H4>Jak to funguje?</H4>
<p>
Zařízení v LAN síti spolu komunikují pomocí MAC adres, unikátních adres každého zařízení přidělených výrobcem. Každá bezdrátová karta a přístupový bod mají svoji MAC adresu. Pokud zařízení odesílá data, připojí svoji MAC adresu k odesílanému datovému rámci, aby příjemce rámce věděl, kdo je odesilatelem. Takže přenášené datové rámce obsahují MAC adresu odesilatele i cílového zařízení.</p>

<p>
Pokud jsou data přenášena ethernetem, jsou potřeba pouze dvě MAC adresy - odesilatel a příjemce. Pokud jsou přenášena mezi dvěmi stanicemi, které nejsou připojené do stejného segmentu LAN (tedy jsou na jiných sítích), je zde zapotřebí zařízení, které tyto sítě přemostí a zajistí přechod dat z jednoho segmentu sítě do druhého. Tuto funkci obsarává síťový most, bridge. </p>

<p>
Přístupový bod je právě takový bridge, protože předává data mezi bezdrátovou a kabelovou sítí. K tomu používá tabulku přemostění nazývanou "bridge learn table". V tabulce přemostění jsou uloženy MAC adresy ve spojení se segmentem sítě LAN (nebo fyzického rozhraní), ke kterému z hlediska bridge patří. </p>

<p>
Provoz mezi bezdrátovými zařízeními podle IEEE802.11 tedy vyžaduje znalost čtyř MAC adres namísto dvou, jako je tomu v ethernetu na stejném segmentu. Pokud je bezdrátové zařízení asociováno k přístupovému bodu, bude vždy při přenášení dat skrze přístupový bod používat MAC adresu přístupového bodu jakožto cílovou adresu. MAC adresa skutečné cílové stanice je rovněž připojena v hlavičce rámce, takže přístupový bod může určit, na jakou adresu má rámec dále poslat. A MAC adresa odesílací stanice je v rámci uvedena jako odesílací adresa. </p>

<p>
Takže pokud je WDS spojení mezi dvěmi přístupovými body používáno, jsou všechny čtyři MAC adresy používány:</p>

<UL>
<UL>
<LI>MAC adresa odesilatele</LI>
<LI>MAC adresa cílové stanice</LI>
<LI>MAC adresa přeposílajícího přístupového bodu</LI>
<LI>MAC adresa přijímacího přístupového bodu</LI></UL></UL>
<p>
Tím je také řečeno, co všechno pro sestavení WDS spojení potřebujete znát - prakticky vlastně MAC adresy přístupových bodů ve WDS spojení. A výše uvedené také znamená, že WDS není žádný magický samoorganizující se protokol, jde o fixní směrování datového toku mezi dvěmi MAC adresami a pokud se spojení mezi přístupovými body propojenými via WDS z nějakého vnějšího důvodu přeruší (překážka atd), nelze provoz automaticky převést na jiný sousední přístupový bod a směrovat ho jinudy. To byste toho po WDS chtěli až moc. I tak se s ním za chvíli vyblbneme. </p>

<H4>WDS přemostění versus opakovače</H4>
<p>
WDS lze použít ve dvou základních režimech, přemostění a opakovače. <BR>Při přemostění je pouze předáváno internetové spojení z jednoho přístupového bodu na druhý, není ale povoleno připojení klientů. Naopak při funkci opakovače je možné, aby se distribuovalo nejenom spojení mezi přístupovými body, ale také aby přístupové body poskytovali své služby klientům. Funkce bezdrátového přemostění je zajímavá spíše pro spojení dvou LAN sítí, naopak bezdrátový opakovač je zajímavý pro vytváření většího pokrytí bezdrátovou sítí bez dalších nákladů na připojování jednotlivých přístupových bodů do internetu. </p>

<p>
<STRONG>Nevýhoda:</STRONG> WDS propojuje přístupové body na stejném kanálu, na jakém připojuje klienty. Důvod je jednoduchý - přístupové body nemají dvě radiové části a tak si musí vystačit s prací na jednom kmitočtu. To vede ke snížení propustnosti a zvýšení zarušení, rychlost jde dolů a to je daň za finanční i časovou úsporu. Rychlost na každém skoku bezdrátového opakovače je zhruba polovinou rychlosti přechozího skoku. </p>

<p>
<STRONG>Pozor: žádné dynamické klíče!</STRONG> WDS nepodporuje zajíštění dynamickými klíči, takže funkci WPA musíte vypnout. Je možné používat pouze statické WEP klíče a podle některých praktických zjištění se vyplatí, v případě, že něco nefunguje, vypnout i je. WPA nelze používat ani mezi přístupovými body ani mezi klienty a přístupovými body...</p>

<H4>Příprava</H4>
<p>
Před tím, než si ukážeme praktické postupy při využití WDS, se podíváme na některé zásady práce s WDS. Především nastudujte v manuálu vašeho zařízení, jak a kde se WDS nastavuje. </p>

<p>
Nejprve doporučuji vyzkoušet, zda se klient bez problémů spojí s přístupovým bodem a zda data tečou, jak mají. Je lepší si být jistý základními bezdrátovými a síťovými funkcemi, než začneme experimentovat s WDS. </p>

<p>
<STRONG>Každému AP přiřaďte statickou IP adresu</STRONG><BR>Až budete dumat nad tím, jakému přístupovému bodu přidělilo DHCP zrovna tuhle adresu, přijde vám tato poučka vhod. Takhle vždy budete vědět, jaké AP má jakou IP a tedy kde je problém. Je samozřejmě potřeba dát pozor na to, abyste zvolili IP adresu mimo rozsah, který automaticky přiděluje DHCP, abyste se vyhnuli riziku duplicitní IP adresy. </p>

<p>
<STRONG>Najděte co nejčistší kanál pro všechna AP</STRONG><BR>Je potřeba projít nějakou utilitkou Site Survey jednotlivé kanály a vybrat pokud možno ten nejčistší. Dávejte pozor, abyste nerušili kanál někoho jiného. </p>

<p>
<STRONG>Nastavte pro všechny AP různé SSID (není nutné, jen ušetří nervy při ladění)</STRONG><BR>Tahle rada může vypadat zvláštně, ale pro první testování se vyplatí mít přehled. Jednotlivé AP se samy mezi sebou poznají podle MAC adresy, ale vy si MAC adresu asi pamatovat nebudete, takže je vhodné si jednotlivá AP pojmenovat, abyste věděli, ke kterému se připojujete, protože klientský software vypisuje SSID. </p>

<p>
Výhodou nastavení rozdílných SSID je také fakt, že Zero Configuration utilita u Windows XP vám poctivě vypíše všechny přístupové body, které máte v dosahu. Pokud budou mít stejné SSID, nepoznáte, že jich je více, protože je nevypíše. </p>

<p>
<STRONG>Nastavte klientovi statickou IP (není nutné)</STRONG><BR>Přidělení IP přes DHPC často trvá a nefunguje tak spolehlivě, jak bychom potřebovali. Pokud přidělíte statickou IP, DNS a bránu, ušetříte síti jeden krok, který může nedopadnout. Někdy se totiž stane, že DHCP přidělení neprojde přes nějaký most. </p>

<p>
Ještě jednou zdůrazňuji optimalizaci signálu - rychlost WDS závisí na kvalitě signálu. </p>

<H4>Hrátky s MAC adresami</H4>
<p>
Nyní přichází samotné Opus Magnum. Zde je třeba říci, že některé produkty nevyžadují, aby se zadávaly MAC adresy, prostě se propojí s WDS AP ve svém dosahu. Je ale lepší zablokování na konkrétní MAC adresy zapnout, protože tím ztížíte nepovolaným AP možnost propašovat se do vaší sítě. Navíc se považuje blokování na MAC adresy za "standardnější", takže s ním lépe fungují výrobky rozdílných výrobců, pokud vůbec fungují. </p>

<p>
Pokud používáte XPčka, jste v trochu prekérní situaci, protože Zero config utilita nikde nepíše MAC adresu přístupového bodu. MAC adresa v Zero config je adresa klientského adaptéru a ta je nám na nic. Nejlepší bude spustit utilitku dodávanou výrobcem k síťové kartě, nebo program NetStumbler - minimálně ten je schopný detekovat MAC adresu přístupového bodu. Když bude nejhůř, najdete MAC adresu na přístupovém bodu napsanou :)</p>

<p>
Na obrázku je příklad Site Survey programu dodávaného k NETGEAR WG511T. </p>

<P align=center><IMG height=272 alt="Site Survey u karty Netgear" src="/wp-content/uploads/wds-netgear.jpg" width=450 align=center border=1></p>

<p>
&#160;</p>

<p>
Díky tomu jsme zjistili, že nás zajímají dva přístupové body:<BR>Belkin F5D7130 <STRONG>ssid:</STRONG> belkin54g_1 <STRONG>MAC:</STRONG> 00 30 BD 91 BB FA <BR>ASUS WL300g <STRONG>ssid:</STRONG> WL300g <STRONG>MAC:</STRONG> 00 0C 6E 34 9A AE </p>

<p>
Oba tyto přístupové body podporují WDS a prodávají se u nás, takže si to na nich ukážeme. </p>

<H4>WDS - jeden přeskok</H4>
<p>
Na obrázku vidíte, jak vypadá zapojení s jedním přeskokem pomocí WDS. Máme tu dva přístupové body (zmíněný Belkin F5D7130 a <A href="/wifidetail.html?id=309">Asus WL300g</A>, oba používají Broadcom čipset BCM4702), přičemž internet je zaveden pouze do Belkina a propojení klienta zařizuje Asus funkcí WDS. </p>

<P align=center><IMG height=372 alt="Jeden přeskok s WDS" src="/wp-content/uploads/wds-jedenskok.jpg" width=375></p>

<p>
&#160;</p>

<p>
Na následujícím obrázku vidíte, jak <STRONG>nastavení WDS probíhá ve web administraci Belkinu</STRONG>. Nastavování provádějte klidně tak, že si přístupový bod připojíte kabelem do ethernetu, nemá smysl se strápit s tím, jak to rozchodit bezdrátově :)</p>

<P align=center><IMG height=361 alt="nastavení WDS na Belkinu" src="/wp-content/uploads/wds3-belkin" width=450 border=1></p>

<p>
Horní dvě volby povolují bezdrátové přemostění a zamykají toto přemostění pouze pro zadané MAC adresy. Poslední volbou byste zakázali připojení bezdrátových klientů na přístupový bod. Pokud byste tuto volbu zaškrtli, fungoval by pouze jako bezdrátový most, nikoliv jako bezdrátový opakovač, což potřebujeme. </p>

<p>
A na následujícím obrázku vidíme, jak se totéž <STRONG>nastavuje na přístupovém bodu Asus</STRONG>. Asus používá dokonce grafiku, aby znázornil, jaký režim používání si můžete vybrat: AP Mode, WDS only a Hybrid. AP mode je klasický režim přístupového bodu, zatímco WDS only je pouze bezdrátové přemostění bez možnosti připojovat klienty. To umí až Hybrid mode - tak ho zvolte. </p>

<P align=center><IMG height=385 alt="nastavení WDS na Asus" src="/wp-content/uploads/wds4-asuswl300g" width=450 border=1></p>

<p>
Dále nastavujete, zda povolíte připojit se na AP v Remote Bridge List (ten se nastavuje o kousek níže, vyplníte tam MAC adresy) a zda povolíte anonymní připojení. Nastavení u Belkinu mi přijde o trochu přehlednější a jasnější. </p>

<p>
Na obrázku tedy vidíte správně nakonfigurovaný ASUS přístupový bod, který nyní bude sloužit jak pro připojení klientů, tak pro propojení WDS s přístupovým bode udané MAC adresy. </p>

<H4>Funguje to?</H4>
<p>
Nyní se pojďme podívat, jak nám to funguje. Prvním příznakem správně fungujícího propojení by měly být zuřivě blikající LEDky na přístupových bodech i síťovém switchi, do něhož jsme zapojili Belkin. Samozřejmě odpojte ethernetový kabel, který jsme používali ke konfiguraci Asusu - zapojení by mělo odpovídat obrázku o dva výše. </p>

<p>
Nyní si vyzkoušejme z počítače připojeného mimo Asus pingnout na IP adresu Asusu - spusťte si DOS okno a dejte <FONT face="Courier CE, Courier"><STRONG>PING 192.168.3.230</STRONG></FONT> (pro náš případ). Pokud se začnou vracet číselné odezvy o pingu, WDS propojení funguje. Nyní můžete přístupové body umístit do pozic, kde mají fungovat, zapojit je a přesvědčit se, že spojení mezi nimi stále funguje. Pokud ne, máte problém s dosahem...</p>

<H4>Co s problémy</H4>
<p>
Pokud PING nefunguje, zkuste ho ještě po minutě, někdy se stává, že se zařízení mezi sebou chvilku hádají, než se "chytí" a je zbytečné hned všechno začít předělávat. </p>

<p>
Pokud to nepomohlo, znovu projděte nastavení obou AP, především se přesvěčte, že jste správně zadali a opsali MAC adresy. Pokud tato kontrola nepomůže a zařízení jsou ve vzdálenosti, kdy můžeme čekat, že mezi sebou mají radiový dosah, máte asi smůlu a padli jste na dva kusy, které spolu nespolupracují. Než je rozšlapete, znovu zkontrolujte nastavení obou kousků a zejména MAC adresy - častá je záměna nuly za O - óčko se v MAC adrese nepoužívá, protože ta je hexadecimální. A taky záměna B za 8... </p>

<H4>WDS se dvěmi přeskoky</H4>
<p>
A nyní si zkusíme něco maličko těžšího, abychom se ujistili, že chápeme, jak se WDS sestavuje. Zkusíme si propojení se dvěmi přeskoky. </p>

<P align=center><IMG height=470 alt="WDS se dvěmi přeskoky" src="/wp-content/uploads/wds6-trihopy" width=382 align=center></p>

<p>
V tomto případě <STRONG>je třetím APčkem ASUS WL330</STRONG> - tím si vyzkoušíme, jak spolupracují různé čipové sady a rychlosti 802.11g a 802.11b. Do sítě nám tedy přibude následující konfigurace:</p>

<p>
ASUS WL330&#160;<STRONG>ssid:</STRONG> WL330&#160;<STRONG>MAC:</STRONG> 00 0E A6 22 A2 14</p>

<p>
Na obrázku vidíme, jak musíme <STRONG>upravit konfiguraci druhého APčka</STRONG>, tedy toho původního Asus WL300G. Jak vidíte, přidali jsme do sekce Remote Bridge List MAC adresu nového přístupového bodu. </p>

<P align=center><IMG height=385 alt="WDS konfigurace asusu" src="/wp-content/uploads/wds7-asus3hopy" width=450 border=1></p>

<p>
Na následujícím obrázku vidíme, jak musíme nastavit konfiguraci třetího přístupového bodu, Asus WL330. Také si povšimnete (na obrázku to není vidět), že Asus WL330 nepodporuje režim WDS only, tedy režim pouze bezdrátového mostu. Na výběr je pouze klasický režim AP a režim WDS propojení a připojení klientů. </p>

<P align=center><IMG height=403 alt="nastavení WDS na dalším Asusu" src="/wp-content/uploads/wds8-wl330_setup" width=450 border=1></p>

<p>
Po uložení nastavení by celá síť měla zase fungovat, ovšem s tím, že přenosová rychlost, jakou lze dosáhnout na posledním přístupovém bodu, stěží dosahuje 2 Mb/s. </p>

<H4>Zapojování více WDS zařízení: řetězení, hvězda a kruh</H4>
<p>
Na uvedeném příkladě jsme si ukázali nejběžnější zapojení více WDS zařízení - <STRONG>řetězení</STRONG>, kdy jedno AP je připojeno na předešlé a případně na následující. Takto lze internet rozvést i na velké vzdálenosti, stačí připojit větší antény a slučovače pro antény. </p>

<p>
Pokud je k jednomu přístupovému bodu připojeno více dalších přístupových bodů mezi sebou vzájemně nepropojených, hovoříme o <STRONG>uspořádání do hvězdy</STRONG>, viz obrázek. Hlavní výhodou uspořádání je fakt, že k připojenému AP je to pouze jeden přeskok, takže přenosová rychlost se snižuje pouze na polovinu. Nevýhodou samozřejmě je to, že pokud přístupový bod s internetovým připojením vypadne, jsou i ostatní přístupové body bez internetu. </p>

<P align=center><IMG height=512 alt="WDS uspořádání do hvězdy" src="/wp-content/uploads/wds-hvezda.jpg" width=336 align=center></p>

<p>
&#160;</p>

<p>
Pokud se koncová a počáteční zařízení propojená do řetězce stýkají, mluvíme o <STRONG>propojení do kruhu</STRONG>. I v tomto případě je klíčovým bodem APčko s přivedeným internetem, to když spadne, tak je problém. Na druhou stranu, pokud spadne jakýkoliv jiný AP, mohou data proudit z druhé strany kruhu. </p>

<P align=center><IMG height=511 alt="WDS uspořádané do kruhu" src="/wp-content/uploads/wds-kruh.jpg" width=298></p>

<p>
&#160;</p>

<p>
Pokud hodláte používat kruhovou architekturu, musí vaše přístupové body podporovat <A href="http://archiv.isdn.cz//a93/a345c120.php3" target=_blank>spanning tree protokol</A> (STP), což už je případ jen těch dražších (Orinoco/Proxim AP-2000/2500, <A href="/wifidetail.html?id=209">Buffalo WLM2-G54</A>, Avaya atd, ale také laciný <A href="/wifidetail.html?id=203">OvisLink WL-1120AP</A>). Pokud se pokusíte tak zapojit obyčejný WDS AP, nebude to fungovat, protože se data budou hádat, kam vlastně mají putovat. </p>

<H4>Závěrem</H4>
<p>
Jak vidíte, je WDS poměrně mocný spoluhráč při výstavbě bezdrátové sítě. Na druhou stranu je třeba si uvědomit, že každý přeskok snižuje datovou propustnost na polovinu předchozího a aby toho nebylo dost, jednotlivý výrobci omezují počet AP, která spolu takto mohou fungovat na čtyř, šest nebo osm - možná časem narazíte i na jiná čísla. WDS velmi silně doporučuji používat jen v rámci stejného výrobce a stejného modelu, pokud chcete kupovat mermomocí rozdílné výrobky, zkuste si zjistit, zda mají stejnou čipovou sadu. </p>

<p>
Pomocí WDS můžete ušetřit nákup a propojování více zařízení. Můžete takto například propojit několik budov, přičemž internet je přivede pouze do jedné z nich a mezi některými budovami není přímá viditelnost, takže se nedá použít připojení na centrální přístupový bod. Vaší fantazii se meze nekladou. </p>

</p>